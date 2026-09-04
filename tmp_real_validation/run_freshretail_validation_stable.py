#!/usr/bin/env python3
from __future__ import annotations
import json, math, time
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import linprog
from scipy.stats import beta as beta_dist, binom
from huggingface_hub import hf_hub_download

OUT=Path('freshretail_stable_output'); OUT.mkdir(exist_ok=True)
SEED=20260904; rng=np.random.default_rng(SEED)
ALPHA=.60; GAMMA=.20; BETA_CONF=.05
DEPTHS=[2,4,6,8,12,16,24,32]; REPS=40
# Population bounds independently certified by Chebyshev dual + high-precision
# Bernstein subdivision, with independent primal lower bounds.
POP_CERT={
2:0.4681643730567352,
4:0.39323415599093553,
6:0.3198009866080933,
8:0.28592548186191963,
12:0.24412887662590457,
16:0.22319556116866235,
24:0.19599949141427533,
32:0.18096409627341062,
}

_BCACHE={}
def Bmat(n,v):
    v=np.asarray(v,float); key=(n,len(v),float(v[0]),float(v[-1])) if len(v)>1 else None
    return np.vstack([binom.pmf(k,n,v) for k in range(n+1)])

def split_bern(c,t):
    # de Casteljau subdivision; longdouble keeps the continuous feasibility check
    # stable even when the optimizer's Bernstein coefficients are large.
    c=np.asarray(c,dtype=np.longdouble); t=np.longdouble(t); n=len(c)-1
    tri=[c.copy()]
    for r in range(1,n+1):
        prev=tri[-1]; tri.append((1-t)*prev[:-1]+t*prev[1:])
    left=np.array([tri[r][0] for r in range(n+1)],dtype=np.longdouble)
    right=np.array([tri[n-r][r] for r in range(n+1)],dtype=np.longdouble)
    return left,right

def subdiv_cert_lower(c,maxdepth=16,accept=-1e-12):
    pending=[np.asarray(c,dtype=np.longdouble)]; leaves=[]
    for depth in range(maxdepth+1):
        nxt=[]
        for z in pending:
            mz=np.min(z)
            if mz>=accept or depth==maxdepth:
                leaves.append(mz)
            else:
                L,R=split_bern(z,np.longdouble('0.5')); nxt.extend([L,R])
        if not nxt: break
        pending=nxt
    return float(min(leaves)) if leaves else 0.0

def continuous_correction(d,alpha):
    L,R=split_bern(d,np.longdouble(str(alpha)))
    # constant one has Bernstein coefficients all equal to one
    lbL=subdiv_cert_lower(L,maxdepth=16)
    lbR=subdiv_cert_lower(R-np.longdouble(1.0),maxdepth=16)
    # add a small floating-point safety pad after the long-double certificate
    safety=2e-9
    corr=max(0.0,-lbL,-lbR)+safety
    return corr,lbL,lbR,float(np.max(np.abs(np.asarray(d,float))))

def band_upper_stable(counts,alpha,beta_conf=.05):
    counts=np.asarray(counts,float); S=int(counts.sum()); freq=counts/S; n=len(counts)-1
    rho=math.sqrt(.5/S*math.log(2*(n+1)/beta_conf)); lo=np.maximum(0,freq-rho); hi=np.minimum(1,freq+rho)
    # A denser starting grid plus two refinement rounds keeps the final certificate
    # correction small; all evaluations remain in Bernstein form.
    grid=np.unique(np.r_[np.linspace(0,1,1201),alpha])
    last=None
    for it in range(3):
        B=Bmat(n,grid); h=(grid>=alpha).astype(float)
        obj=np.r_[1.,hi,-lo]
        Aub=np.column_stack([-np.ones(len(grid)),-B.T,B.T])
        bounds=[(None,None)]+[(0,None)]*(2*(n+1))
        res=linprog(obj,A_ub=Aub,b_ub=-h,bounds=bounds,method='highs')
        if not res.success: raise RuntimeError(f'n={n}: {res.message}')
        eta=res.x[0]; aa=res.x[1:n+2]; bb=res.x[n+2:]; d=eta+aa-bb
        # Locate likely missed minima by direct, stable Bernstein evaluation.
        vg=np.unique(np.r_[np.linspace(0,1,8001),alpha]); q=np.asarray(d@Bmat(n,vg),float); hg=(vg>=alpha).astype(float); gap=q-hg
        badidx=np.argsort(gap)[:8]; new=vg[badidx]
        grid=np.unique(np.r_[grid,new])
        last=(res,d)
    res,d=last
    corr,lbL,lbR,maxc=continuous_correction(d,alpha)
    return min(1.,float(res.fun+corr)),rho,{'raw':float(res.fun),'corr':corr,'lb_left':lbL,'lb_right_minus1':lbR,'max_abs_bern_coeff':maxc}

def beta_tail(K,n,alpha):
    K=np.asarray(K,float); m1=float(np.mean(K/n)); m2=float(np.mean(K*(K-1)/(n*(n-1)))) if n>=2 else m1*m1
    var=max(0.,m2-m1*m1)
    if m1<=1e-12:return 0.
    if m1>=1-1e-12:return 1.
    conc=1e6 if var<=1e-10 else max(1e-4,m1*(1-m1)/var-1)
    return float(beta_dist.sf(alpha,max(1e-6,m1*conc),max(1e-6,(1-m1)*conc)))

def main():
    tp=hf_hub_download('Dingdong-Inc/FreshRetailNet-50K','data/train.parquet',repo_type='dataset'); ep=hf_hub_download('Dingdong-Inc/FreshRetailNet-50K','data/eval.parquet',repo_type='dataset')
    cols=['store_id','product_id','dt','stock_hour6_22_cnt']; tr=pd.read_parquet(tp,columns=cols); ev=pd.read_parquet(ep,columns=cols)
    tr['event']=(tr.stock_hour6_22_cnt>0).astype(np.uint8); ev['event']=(ev.stock_hour6_22_cnt>0).astype(np.uint8)
    tr=tr.sort_values(['store_id','product_id','dt']); ev=ev.sort_values(['store_id','product_id','dt'])
    N=tr[['store_id','product_id']].drop_duplicates().shape[0]; X=tr.event.to_numpy().reshape(N,90); E=ev.event.to_numpy().reshape(N,7)
    full_rate=X.mean(1); eval_rate=E.mean(1); truth=float(np.mean(full_rate>=ALPHA)); future=float(np.mean(eval_rate>=ALPHA))
    rows=[]; t0=time.time()
    for n in DEPTHS:
        for rep in range(REPS):
            idx=rng.integers(0,90,size=(N,n)); K=np.take_along_axis(X,idx,axis=1).sum(1).astype(int)
            cnt=np.bincount(K,minlength=n+1); plug=float(np.mean(K/n>=ALPHA)); bt=beta_tail(K,n,ALPHA); ru,rho,diag=band_upper_stable(cnt,ALPHA,BETA_CONF)
            rows.append({'depth':n,'rep':rep,'full90_tail':truth,'eval7_tail':future,'population_identified_upper':POP_CERT[n],
                         'plug_in_tail':plug,'beta_binomial_tail':bt,'robust_upper':ru,'rho':rho,'gamma':GAMMA,'alpha':ALPHA,
                         'robust_raw_dual':diag['raw'],'robust_cert_correction':diag['corr'],'robust_cert_lb_left':diag['lb_left'],
                         'robust_cert_lb_right_minus1':diag['lb_right_minus1'],'robust_max_abs_bern_coeff':diag['max_abs_bern_coeff']})
        print('done depth',n,'median robust',np.median([r['robust_upper'] for r in rows if r['depth']==n]),flush=True)
    raw=pd.DataFrame(rows); raw.to_csv(OUT/'freshretail_validation_raw_stable.csv',index=False)
    summ=raw.groupby('depth').agg(full90_tail=('full90_tail','first'),eval7_tail=('eval7_tail','first'),population_identified_upper=('population_identified_upper','first'),
        plug_median=('plug_in_tail','median'),plug_p10=('plug_in_tail',lambda x:np.quantile(x,.1)),plug_p90=('plug_in_tail',lambda x:np.quantile(x,.9)),
        beta_median=('beta_binomial_tail','median'),robust_median=('robust_upper','median'),robust_p10=('robust_upper',lambda x:np.quantile(x,.1)),robust_p90=('robust_upper',lambda x:np.quantile(x,.9)),
        rho=('rho','first'),max_cert_correction=('robust_cert_correction','max'),median_cert_correction=('robust_cert_correction','median'),max_abs_bern_coeff=('robust_max_abs_bern_coeff','max')).reset_index()
    summ.to_csv(OUT/'freshretail_validation_summary_stable.csv',index=False)
    audit={'source':'Dingdong-Inc/FreshRetailNet-50K','series':int(N),'alpha':ALPHA,'gamma':GAMMA,'beta_conf':BETA_CONF,'reps':REPS,'depths':DEPTHS,
        'full90_tail':truth,'eval7_tail':future,'population_bounds':POP_CERT,'population_monotone':bool(np.all(np.diff([POP_CERT[n] for n in DEPTHS])<=0)),
        'max_finite_sample_certificate_correction':float(raw.robust_cert_correction.max()),'elapsed_sec':time.time()-t0,'seed':SEED,
        'method_note':'Finite-sample robust dual solved in count-law Bernstein coordinates; continuous-domain feasibility certified directly by long-double de Casteljau subdivision on [0,alpha] and [alpha,1], avoiding Bernstein-to-power conversion.'}
    (OUT/'freshretail_stable_audit.json').write_text(json.dumps(audit,indent=2)); print(json.dumps(audit,indent=2)); print(summ.to_string(index=False))
if __name__=='__main__':main()
