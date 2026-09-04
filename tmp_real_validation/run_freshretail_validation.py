#!/usr/bin/env python3
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import linprog
from scipy.interpolate import BPoly, PPoly
from scipy.stats import beta as beta_dist, binom
from huggingface_hub import hf_hub_download

OUT=Path('real_validation_output'); OUT.mkdir(exist_ok=True)
SEED=20260904; rng=np.random.default_rng(SEED); _BERN={}

def bernstein_matrix(n,ngrid=401):
    key=(n,ngrid)
    if key not in _BERN:
        v=np.linspace(0,1,ngrid); B=np.vstack([binom.pmf(k,n,v) for k in range(n+1)]); _BERN[key]=(v,B)
    return _BERN[key]

def minbern(c,a,b):
    pp=PPoly.from_bernstein_basis(BPoly(np.asarray(c,float)[:,None],[0.,1.])); r=np.asarray(pp.derivative().roots(extrapolate=False));
    rr=r[np.abs(np.imag(r))<1e-8].real if r.size else np.array([]); rr=rr[(rr>=a-1e-12)&(rr<=b+1e-12)]; x=np.r_[a,b,rr]; return float(np.min(pp(x)))

def band_upper(counts,alpha,beta_conf=.05):
    counts=np.asarray(counts,float); S=int(counts.sum()); freq=counts/S; n=len(counts)-1; v,B=bernstein_matrix(n); h=(v>=alpha).astype(float)
    rho=math.sqrt(.5/S*math.log(2*(n+1)/beta_conf)); lo=np.maximum(0,freq-rho); hi=np.minimum(1,freq+rho)
    obj=np.r_[1.,hi,-lo]; Aub=np.column_stack([-np.ones(len(v)),-B.T,B.T]); bounds=[(None,None)]+[(0,None)]*(2*(n+1))
    res=linprog(obj,A_ub=Aub,b_ub=-h,bounds=bounds,method='highs')
    if not res.success: raise RuntimeError(res.message)
    eta=res.x[0]; aa=res.x[1:n+2]; bb=res.x[n+2:]; d=eta+aa-bb; corr=max(0.,-minbern(d,0,alpha),1-minbern(d,alpha,1))
    return min(1.,float(res.fun+corr)),rho

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
    keys=tr[['store_id','product_id']].drop_duplicates(); N=len(keys)
    X=tr.event.to_numpy().reshape(N,90); E=ev.event.to_numpy().reshape(N,7)
    alpha=.50; gamma=.35; beta_conf=.05; full_rate=X.mean(1); eval_rate=E.mean(1); truth=float(np.mean(full_rate>=alpha)); future=float(np.mean(eval_rate>=alpha))
    depths=[2,4,6,8,12,16,24,32,48,64]; reps=40; rows=[]
    for n in depths:
        for rep in range(reps):
            # independent random masking within each real store-product history, without replacement
            U=rng.random((N,90)); idx=np.argpartition(U,n-1,axis=1)[:,:n]; K=np.take_along_axis(X,idx,axis=1).sum(1).astype(int)
            cnt=np.bincount(K,minlength=n+1); plug=float(np.mean(K/n>=alpha)); bt=beta_tail(K,n,alpha); ru,rho=band_upper(cnt,alpha,beta_conf)
            rows.append({'depth':n,'rep':rep,'full90_tail':truth,'eval7_tail':future,'plug_in_tail':plug,'beta_binomial_tail':bt,'robust_upper':ru,'rho':rho,'gamma':gamma,'alpha':alpha})
    raw=pd.DataFrame(rows); raw.to_csv(OUT/'freshretail_validation_raw.csv',index=False)
    summ=raw.groupby('depth').agg(full90_tail=('full90_tail','first'),eval7_tail=('eval7_tail','first'),plug_median=('plug_in_tail','median'),plug_p10=('plug_in_tail',lambda x:np.quantile(x,.1)),plug_p90=('plug_in_tail',lambda x:np.quantile(x,.9)),beta_median=('beta_binomial_tail','median'),robust_median=('robust_upper','median'),robust_p10=('robust_upper',lambda x:np.quantile(x,.1)),robust_p90=('robust_upper',lambda x:np.quantile(x,.9)),rho=('rho','first')).reset_index(); summ.to_csv(OUT/'freshretail_validation_summary.csv',index=False)
    meta={'source':'Dingdong-Inc/FreshRetailNet-50K','series':N,'train_days':90,'eval_days':7,'alpha':alpha,'gamma':gamma,'beta_conf':beta_conf,'reps':reps,'depths':depths,'full90_tail':truth,'eval7_tail':future,'train_stockout_day_fraction':float(X.mean()),'eval_stockout_day_fraction':float(E.mean()),'seed':SEED,'design_note':'Retrospective shallow-history masking without replacement; full 90-day train history is the empirical benchmark. Eval 7-day tail is a temporal-shift stress test, not a precise latent-risk estimate.'}; (OUT/'freshretail_meta.json').write_text(json.dumps(meta,indent=2)); print(json.dumps(meta,indent=2)); print(summ.to_string(index=False))
if __name__=='__main__':main()
