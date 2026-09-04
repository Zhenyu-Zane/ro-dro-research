#!/usr/bin/env python3
from __future__ import annotations
import json, warnings
from pathlib import Path
import numpy as np
import pandas as pd
import cvxpy as cp
from huggingface_hub import hf_hub_download

OUT=Path('sdp_check_output'); OUT.mkdir(exist_ok=True)
DEPTHS=[2,4,6,8,12,16,24,32]
ALPHA=.60; A=2*ALPHA-1


def M(seq,d):
    return cp.bmat([[seq[i+j] for j in range(d+1)] for i in range(d+1)])

def G(seq,d,l,u):
    # localizing matrix for (x-l)(u-x) = -x^2 + (l+u)x - lu
    return cp.bmat([[-seq[i+j+2]+(l+u)*seq[i+j+1]-l*u*seq[i+j] for j in range(d+1)] for i in range(d+1)])

def numeric_M(y,d):
    return np.array([[y[i+j] for j in range(d+1)] for i in range(d+1)],float)

def numeric_G(y,d,l,u):
    return np.array([[-y[i+j+2]+(l+u)*y[i+j+1]-l*u*y[i+j] for j in range(d+1)] for i in range(d+1)],float)

def solve_upper(m,n,solver):
    if n%2: raise ValueError('only even n used here')
    d=n//2
    yl=cp.Variable(n+1); yr=cp.Variable(n+1)
    cons=[yl+yr==m, M(yl,d)>>0, M(yr,d)>>0]
    if d>=1:
        cons += [G(yl,d-1,-1.,A)>>0, G(yr,d-1,A,1.)>>0]
    prob=cp.Problem(cp.Maximize(yr[0]),cons)
    kwargs={}
    if solver=='CLARABEL': kwargs=dict(max_iter=1000,tol_gap_abs=1e-10,tol_gap_rel=1e-10,tol_feas=1e-10)
    elif solver=='SCS': kwargs=dict(eps=2e-8,max_iters=500000,acceleration_lookback=20)
    elif solver=='CVXOPT': kwargs=dict(abstol=1e-9,reltol=1e-9,feastol=1e-9,max_iters=500)
    val=prob.solve(solver=solver,verbose=False,**kwargs)
    if prob.status not in ('optimal','optimal_inaccurate'):
        raise RuntimeError(f'{solver} n={n}: {prob.status}')
    l=np.asarray(yl.value,float); r=np.asarray(yr.value,float)
    eigs=[np.min(np.linalg.eigvalsh(numeric_M(l,d))),np.min(np.linalg.eigvalsh(numeric_M(r,d)))]
    if d>=1:
        eigs += [np.min(np.linalg.eigvalsh(numeric_G(l,d-1,-1.,A))),np.min(np.linalg.eigvalsh(numeric_G(r,d-1,A,1.)))]
    return float(val),{'status':prob.status,'moment_resid':float(np.max(np.abs(l+r-m))),'min_psd_eig':float(np.min(eigs))}

def main():
    tp=hf_hub_download('Dingdong-Inc/FreshRetailNet-50K','data/train.parquet',repo_type='dataset')
    tr=pd.read_parquet(tp,columns=['store_id','product_id','dt','stock_hour6_22_cnt'])
    tr['event']=(tr.stock_hour6_22_cnt>0).astype(np.uint8); tr=tr.sort_values(['store_id','product_id','dt'])
    N=tr[['store_id','product_id']].drop_duplicates().shape[0]
    X=tr.event.to_numpy().reshape(N,90); x=2*X.mean(1)-1
    installed=cp.installed_solvers(); print('installed',installed,flush=True)
    solvers=[s for s in ['CLARABEL','CVXOPT','SCS'] if s in installed]
    rows=[]
    for n in DEPTHS:
        m=np.array([np.mean(x**k) for k in range(n+1)])
        row={'depth':n}
        for s in solvers:
            try:
                val,diag=solve_upper(m,n,s)
                row[s.lower()+'_upper']=val; row[s.lower()+'_moment_resid']=diag['moment_resid']; row[s.lower()+'_min_psd_eig']=diag['min_psd_eig']; row[s.lower()+'_status']=diag['status']
            except Exception as e:
                row[s.lower()+'_error']=repr(e)
        rows.append(row); print(row,flush=True)
    df=pd.DataFrame(rows); df.to_csv(OUT/'freshretail_sdp_bounds.csv',index=False)
    audit={'series':int(N),'alpha':ALPHA,'installed_solvers':installed}
    for s in solvers:
        col=s.lower()+'_upper'
        if col in df:
            vals=pd.to_numeric(df[col],errors='coerce').to_numpy(); audit[s+'_monotone_nonincreasing']=bool(np.all(np.diff(vals[np.isfinite(vals)])<=1e-6))
    (OUT/'sdp_audit.json').write_text(json.dumps(audit,indent=2)); print(json.dumps(audit,indent=2))

if __name__=='__main__': main()
