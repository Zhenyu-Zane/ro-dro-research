#!/usr/bin/env python3
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import linprog
from scipy.interpolate import BPoly, PPoly
from scipy.stats import beta as beta_dist, binom

OUT=Path('real_validation_output'); OUT.mkdir(exist_ok=True)
SEED=20260904
rng=np.random.default_rng(SEED)
_BERN={}

def bernstein_matrix(n, ngrid=301):
    key=(n,ngrid)
    if key not in _BERN:
        v=np.linspace(0,1,ngrid)
        B=np.vstack([binom.pmf(k,n,v) for k in range(n+1)])
        _BERN[key]=(v,B)
    return _BERN[key]

def min_bern(coeff,left,right):
    bp=BPoly(np.asarray(coeff,float)[:,None],[0.,1.])
    pp=PPoly.from_bernstein_basis(bp)
    roots=np.asarray(pp.derivative().roots(extrapolate=False))
    rr=roots[np.abs(np.imag(roots))<1e-8].real if roots.size else np.array([])
    rr=rr[(rr>=left-1e-12)&(rr<=right+1e-12)]
    pts=np.r_[left,right,rr]
    vals=np.asarray(pp(pts),float)
    return float(vals[int(np.argmin(vals))])

def band_upper(counts, alpha, beta_conf=0.05, ngrid=301):
    counts=np.asarray(counts,float); S=int(counts.sum()); freq=counts/S; n=len(counts)-1
    v,B=bernstein_matrix(n,ngrid); h=(v>=alpha).astype(float)
    rho=math.sqrt(0.5/S*math.log(2.0*(n+1)/beta_conf))
    lo=np.maximum(0.0,freq-rho); hi=np.minimum(1.0,freq+rho)
    obj=np.r_[1.0,hi,-lo]
    Aub=np.column_stack([-np.ones(len(v)),-B.T,B.T])
    bounds=[(None,None)]+[(0,None)]*(2*(n+1))
    res=linprog(obj,A_ub=Aub,b_ub=-h,bounds=bounds,method='highs')
    if not res.success: raise RuntimeError(res.message)
    eta=float(res.x[0]); aa=np.asarray(res.x[1:n+2]); bb=np.asarray(res.x[n+2:])
    d=eta+aa-bb
    corr=max(0.,-min_bern(d,0.,alpha),1.-min_bern(d,alpha,1.))
    return min(1.,float(res.fun+corr)),rho

def beta_tail_from_counts(K,n,alpha):
    K=np.asarray(K,float); m1=float(np.mean(K/n))
    if n<2: return float('nan')
    m2=float(np.mean(K*(K-1)/(n*(n-1))))
    var=max(0.,m2-m1*m1)
    if m1<=1e-10: return 0.0
    if m1>=1-1e-10: return 1.0
    maxvar=m1*(1-m1)
    conc=1e6 if var<=1e-9 else max(1e-3,maxvar/var-1.)
    return float(beta_dist.sf(alpha,max(1e-6,m1*conc),max(1e-6,(1-m1)*conc)))

def select_monotone(candidates,evaluator,target):
    lo,hi=0,len(candidates)-1
    hi_val=evaluator(candidates[hi])
    if hi_val>target: return float(candidates[hi]),False,float(hi_val)
    while lo<hi:
        mid=(lo+hi)//2
        if evaluator(candidates[mid])<=target: hi=mid
        else: lo=mid+1
    val=evaluator(candidates[lo]); return float(candidates[lo]),True,float(val)

def main():
    url='https://raw.githubusercontent.com/Niloy-Chakraborty/Time-Series_Clustering_For_Smart_Meter_Dataset/master/Main_df.csv'
    df=pd.read_csv(url)
    wcols=[c for c in df.columns if c.startswith('Weekly_Consumption_')]
    X=df[wcols].apply(pd.to_numeric,errors='coerce').to_numpy(float)
    ids=df['Household_Name'].astype(str).to_numpy()
    good=np.sum(np.isfinite(X),axis=1)>=len(wcols)-2
    X=X[good]; ids=ids[good]
    miss=int(np.sum(~np.isfinite(X)))
    med=np.nanmedian(X,axis=1); ii,jj=np.where(~np.isfinite(X)); X[ii,jj]=med[ii]
    N,T=X.shape; alpha=0.10; gamma=0.20; beta_conf=0.05
    depths=[2,4,6,8,12,16,24,32]; reps=60; train_frac=0.70
    rows=[]
    for rep in range(reps):
        perm=rng.permutation(N); m=int(train_frac*N); tr=perm[:m]; te=perm[m:]
        Xtr=X[tr]; Xte=X[te]
        def test_bad(q): return float(np.mean(np.mean(Xte>q,axis=1)>=alpha))
        oracle_cands=np.unique(np.r_[0.,Xte.ravel()])
        q_oracle,_,_=select_monotone(oracle_cands,test_bad,gamma)
        for n in depths:
            if n>T: continue
            cols=np.vstack([rng.choice(T,size=n,replace=False) for _ in range(len(tr))])
            Y=np.take_along_axis(Xtr,cols,axis=1); cands=np.unique(np.r_[0.,Y.ravel()])
            q_pool=float(np.quantile(Y.ravel(),1-alpha,method='higher'))
            def plug(q): return float(np.mean(np.mean(Y>q,axis=1)>=alpha))
            q_plug,_,plug_stat=select_monotone(cands,plug,gamma)
            cache_beta={}
            def bt(q):
                k=np.sum(Y>q,axis=1); key=tuple(np.bincount(k,minlength=n+1).tolist())
                if key not in cache_beta: cache_beta[key]=beta_tail_from_counts(k,n,alpha)
                return cache_beta[key]
            q_beta,_,beta_stat=select_monotone(cands,bt,gamma)
            cache_rob={}; cache_rho={}
            def rb(q):
                k=np.sum(Y>q,axis=1); cnt=np.bincount(k,minlength=n+1); key=tuple(cnt.tolist())
                if key not in cache_rob: cache_rob[key],cache_rho[key]=band_upper(cnt,alpha,beta_conf)
                return cache_rob[key]
            q_rob,rob_feas,rob_stat=select_monotone(cands,rb,gamma)
            for method,q,train_stat,cert in [
                ('Pooled',q_pool,float(np.mean(Y>q_pool)),np.nan),
                ('Plug-in',q_plug,plug_stat,np.nan),
                ('Beta-binomial',q_beta,beta_stat,np.nan),
                ('Identification-robust',q_rob,rob_stat,rob_feas)]:
                bad=test_bad(q)
                rows.append({'depth':n,'rep':rep,'method':method,'capacity':q,'training_stat':train_stat,
                    'realized_bad_fraction':bad,'violation':bad>gamma,'capacity_regret_pct':100*(q-q_oracle)/q_oracle,
                    'oracle_capacity':q_oracle,'target_gamma':gamma,'alpha':alpha,'certified_on_training':cert,
                    'train_households':len(tr),'test_households':len(te)})
    raw=pd.DataFrame(rows); raw.to_csv(OUT/'london_validation_raw.csv',index=False)
    summ=(raw.groupby(['depth','method']).agg(
        capacity_median=('capacity','median'),capacity_p10=('capacity',lambda x:np.quantile(x,.1)),capacity_p90=('capacity',lambda x:np.quantile(x,.9)),
        bad_median=('realized_bad_fraction','median'),bad_p90=('realized_bad_fraction',lambda x:np.quantile(x,.9)),
        violation_rate=('violation','mean'),regret_median_pct=('capacity_regret_pct','median'),regret_p90_pct=('capacity_regret_pct',lambda x:np.quantile(x,.9)),
        certification_rate=('certified_on_training',lambda x:np.nanmean(pd.to_numeric(x,errors='coerce'))),n_rep=('rep','count')).reset_index())
    summ.to_csv(OUT/'london_validation_summary.csv',index=False)
    meta={'source_url':url,'households':int(N),'weeks':int(T),'missing_imputed':miss,'alpha':alpha,'gamma':gamma,'beta_conf':beta_conf,
          'reps':reps,'depths':depths,'train_fraction':train_frac,'seed':SEED}
    (OUT/'london_meta.json').write_text(json.dumps(meta,indent=2))
    print(json.dumps(meta,indent=2)); print(summ.to_string(index=False))
if __name__=='__main__': main()
