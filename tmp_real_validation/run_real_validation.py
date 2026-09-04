#!/usr/bin/env python3
from __future__ import annotations
import json, math, time
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

def exact_upper(freq, alpha, ngrid=301):
    p=np.asarray(freq,float); p=p/p.sum(); n=len(p)-1
    v,B=bernstein_matrix(n,ngrid); h=(v>=alpha).astype(float)
    res=linprog(p,A_ub=-B.T,b_ub=-h,bounds=[(None,None)]*(n+1),method='highs')
    if not res.success: raise RuntimeError(res.message)
    d=np.asarray(res.x)
    corr=max(0.,-min_bern(d,0.,alpha),1.-min_bern(d,alpha,1.))
    return min(1.,float(res.fun+corr))

def beta_tail_from_counts(K,n,alpha):
    K=np.asarray(K,float); m1=float(np.mean(K/n))
    if n<2: return float('nan')
    m2=float(np.mean(K*(K-1)/(n*(n-1))))
    var=max(0.,m2-m1*m1)
    if m1<=1e-10: return 0.0
    if m1>=1-1e-10: return 1.0
    maxvar=m1*(1-m1)
    conc=1e6 if var<=1e-9 else max(1e-3,maxvar/var-1.)
    a=max(1e-6,m1*conc); b=max(1e-6,(1-m1)*conc)
    return float(beta_dist.sf(alpha,a,b))

def select_monotone(candidates,evaluator,target):
    lo,hi=0,len(candidates)-1
    if evaluator(candidates[hi])>target: return float(candidates[hi]),False
    while lo<hi:
        mid=(lo+hi)//2
        if evaluator(candidates[mid])<=target: hi=mid
        else: lo=mid+1
    return float(candidates[lo]),True

def london_validation():
    url='https://raw.githubusercontent.com/Niloy-Chakraborty/Time-Series_Clustering_For_Smart_Meter_Dataset/master/Main_df.csv'
    df=pd.read_csv(url)
    wcols=[c for c in df.columns if c.startswith('Weekly_Consumption_')]
    X=df[wcols].apply(pd.to_numeric,errors='coerce').to_numpy(float)
    good=np.sum(np.isfinite(X),axis=1)>=len(wcols)-2
    X=X[good]
    miss=int(np.sum(~np.isfinite(X)))
    med=np.nanmedian(X,axis=1); ii,jj=np.where(~np.isfinite(X)); X[ii,jj]=med[ii]
    S,T=X.shape; alpha=0.10; gamma=0.20
    def badfrac(q): return float(np.mean(np.mean(X>q,axis=1)>=alpha))
    full_cands=np.unique(np.r_[0.,X.ravel()])
    q_oracle,_=select_monotone(full_cands,badfrac,gamma); oracle_bad=badfrac(q_oracle)
    rows=[]; depths=[2,4,6,8,12,16,24,32]; reps=80
    for n in depths:
        if n>T: continue
        for rep in range(reps):
            cols=np.vstack([rng.choice(T,size=n,replace=False) for _ in range(S)])
            Y=np.take_along_axis(X,cols,axis=1); cands=np.unique(np.r_[0.,Y.ravel()])
            q_pool=float(np.quantile(Y.ravel(),1-alpha,method='higher'))
            def plug(q): return float(np.mean(np.mean(Y>q,axis=1)>=alpha))
            q_plug,_=select_monotone(cands,plug,gamma)
            cache_beta={}
            def bt(q):
                k=np.sum(Y>q,axis=1); key=tuple(np.bincount(k,minlength=n+1))
                if key not in cache_beta: cache_beta[key]=beta_tail_from_counts(k,n,alpha)
                return cache_beta[key]
            q_beta,_=select_monotone(cands,bt,gamma)
            cache_rob={}
            def rb(q):
                k=np.sum(Y>q,axis=1); cnt=np.bincount(k,minlength=n+1); key=tuple(cnt.tolist())
                if key not in cache_rob: cache_rob[key]=exact_upper(cnt/cnt.sum(),alpha)
                return cache_rob[key]
            q_rob,rob_feas=select_monotone(cands,rb,gamma)
            for method,q in [('Pooled',q_pool),('Plug-in',q_plug),('Beta-binomial',q_beta),('Identification-robust',q_rob)]:
                rows.append({'depth':n,'rep':rep,'method':method,'capacity':q,
                    'realized_bad_fraction':badfrac(q),'capacity_regret_pct':100*(q-q_oracle)/q_oracle,
                    'oracle_capacity':q_oracle,'oracle_bad_fraction':oracle_bad,'target_gamma':gamma,'alpha':alpha,
                    'certified_on_training': (rb(q)<=gamma if method=='Identification-robust' else np.nan)})
    raw=pd.DataFrame(rows); raw.to_csv(OUT/'london_validation_raw.csv',index=False)
    summ=(raw.groupby(['depth','method']).agg(
        capacity_median=('capacity','median'),capacity_p10=('capacity',lambda x:np.quantile(x,.1)),capacity_p90=('capacity',lambda x:np.quantile(x,.9)),
        bad_median=('realized_bad_fraction','median'),bad_p90=('realized_bad_fraction',lambda x:np.quantile(x,.9)),
        violation_rate=('realized_bad_fraction',lambda x:np.mean(x>gamma)),
        regret_median_pct=('capacity_regret_pct','median'),regret_p90_pct=('capacity_regret_pct',lambda x:np.quantile(x,.9)),n_rep=('rep','count')).reset_index())
    summ.to_csv(OUT/'london_validation_summary.csv',index=False)
    meta={'source_url':url,'households':int(S),'weeks':int(T),'missing_imputed':miss,'alpha':alpha,'gamma':gamma,'reps':reps,'depths':depths,
        'oracle_capacity':float(q_oracle),'oracle_bad_fraction':float(oracle_bad),'seed':SEED}
    (OUT/'london_meta.json').write_text(json.dumps(meta,indent=2))
    return meta

def freshretail_validation():
    from huggingface_hub import hf_hub_download
    path=hf_hub_download(repo_id='Dingdong-Inc/FreshRetailNet-50K',filename='data/train.parquet',repo_type='dataset')
    cols=['store_id','product_id','dt','sale_amount','hours_sale','stock_hour6_22_cnt','hours_stock_status']
    df=pd.read_parquet(path,columns=cols)
    stock=df['stock_hour6_22_cnt'].to_numpy()>0
    frac=float(np.mean(stock))
    g=df.assign(stockout_day=stock).groupby(['store_id','product_id','stockout_day'])['sale_amount'].agg(['mean','count']).reset_index()
    pm=g.pivot(index=['store_id','product_id'],columns='stockout_day',values='mean')
    pc=g.pivot(index=['store_id','product_id'],columns='stockout_day',values='count')
    valid=pm.index[(pc.get(False,0)>=5)&(pc.get(True,0)>=3)]
    r=(pm.loc[valid,True]/pm.loc[valid,False]).replace([np.inf,-np.inf],np.nan).dropna()
    def active_adjust(row):
        hs=np.asarray(row['hours_sale'],dtype=float); st=np.asarray(row['hours_stock_status'],dtype=int)
        if hs.size<23 or st.size<23: return np.nan
        sl=hs[6:23]; ss=st[6:23]; avail=int(np.sum(ss==0))
        if avail<8: return np.nan
        return float(np.sum(sl[ss==0])*17.0/avail)
    sub=df.loc[df['stock_hour6_22_cnt'].between(1,9)].copy()
    if len(sub)>200000: sub=sub.sample(200000,random_state=SEED)
    sub['adjusted_active_sales']=sub.apply(active_adjust,axis=1)
    sub['raw_active_sales']=sub['hours_sale'].map(lambda x: float(np.sum(np.asarray(x,dtype=float)[6:23])))
    ok=(sub['adjusted_active_sales'].notna())&(sub['raw_active_sales']>0)
    uplift=(sub.loc[ok,'adjusted_active_sales']/sub.loc[ok,'raw_active_sales']-1.0)
    summary={'rows':int(len(df)),'series':int(df.groupby(['store_id','product_id']).ngroups),'stockout_day_fraction':frac,
        'paired_series_n':int(len(r)),'stockout_to_nonstockout_mean_sales_ratio_median':float(r.median()),
        'stockout_to_nonstockout_mean_sales_ratio_p25':float(r.quantile(.25)),'stockout_to_nonstockout_mean_sales_ratio_p75':float(r.quantile(.75)),
        'availability_adjusted_proxy_n':int(ok.sum()),'availability_adjusted_uplift_median':float(uplift.median()),
        'availability_adjusted_uplift_p25':float(uplift.quantile(.25)),'availability_adjusted_uplift_p75':float(uplift.quantile(.75))}
    pd.DataFrame([summary]).to_csv(OUT/'freshretail_censoring_summary.csv',index=False)
    (OUT/'freshretail_meta.json').write_text(json.dumps(summary,indent=2))
    return summary

if __name__=='__main__':
    t=time.time(); lm=london_validation(); fr=freshretail_validation()
    allmeta={'london':lm,'freshretail':fr,'elapsed_sec':time.time()-t}
    (OUT/'run_meta.json').write_text(json.dumps(allmeta,indent=2)); print(json.dumps(allmeta,indent=2))
