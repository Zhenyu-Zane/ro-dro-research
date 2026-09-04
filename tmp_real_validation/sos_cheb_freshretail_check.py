#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import pandas as pd
import cvxpy as cp
from numpy.polynomial import chebyshev as C
from huggingface_hub import hf_hub_download

OUT=Path('sos_cheb_output'); OUT.mkdir(exist_ok=True)
DEPTHS=[2,4,6,8,12,16,24,32]
ALPHA=.60; A=2*ALPHA-1


def sos_coeff(Q,r,n):
    out=[0 for _ in range(n+1)]
    for i in range(r+1):
        for j in range(r+1):
            out[i+j] = out[i+j] + 0.5*Q[i,j]
            out[abs(i-j)] = out[abs(i-j)] + 0.5*Q[i,j]
    return out


def mul_cheb(a,g,n):
    out=[0 for _ in range(n+1)]
    for i,ai in enumerate(a):
        for j,gj in enumerate(g):
            if gj==0: continue
            k1=i+j; k2=abs(i-j)
            if k1<=n: out[k1]=out[k1]+0.5*gj*ai
            if k2<=n: out[k2]=out[k2]+0.5*gj*ai
    return out


def g_cheb(l,u):
    # (x-l)(u-x) = -x^2 +(l+u)x -lu = (-1/2-lu)T0 +(l+u)T1 -(1/2)T2
    return [-0.5-l*u, l+u, -0.5]


def solve(m,n,solver):
    d=n//2; c=cp.Variable(n+1)
    Q0L=cp.Variable((d+1,d+1),PSD=True); Q1L=cp.Variable((d,d),PSD=True)
    Q0R=cp.Variable((d+1,d+1),PSD=True); Q1R=cp.Variable((d,d),PSD=True)
    s0L=sos_coeff(Q0L,d,n); s1L=sos_coeff(Q1L,d-1,n); left=[s0L[k]+mul_cheb(s1L,g_cheb(-1.,A),n)[k] for k in range(n+1)]
    s0R=sos_coeff(Q0R,d,n); s1R=sos_coeff(Q1R,d-1,n); right=[s0R[k]+mul_cheb(s1R,g_cheb(A,1.),n)[k] for k in range(n+1)]
    cons=[]
    for k in range(n+1):
        cons.append(c[k]==left[k])
        cons.append(c[k]-(1.0 if k==0 else 0.0)==right[k])
    prob=cp.Problem(cp.Minimize(m@c),cons)
    kwargs={}
    if solver=='CLARABEL': kwargs=dict(max_iter=2000,tol_gap_abs=2e-10,tol_gap_rel=2e-10,tol_feas=2e-10)
    elif solver=='CVXOPT': kwargs=dict(abstol=1e-9,reltol=1e-9,feastol=1e-9,max_iters=500)
    elif solver=='SCS': kwargs=dict(eps=1e-7,max_iters=300000,acceleration_lookback=20)
    val=prob.solve(solver=solver,verbose=False,**kwargs)
    if prob.status not in ('optimal','optimal_inaccurate'): raise RuntimeError(prob.status)
    cv=np.asarray(c.value,float)
    # direct continuous feasibility check from Chebyshev derivative roots
    p=C.Chebyshev(cv); roots=np.asarray(p.deriv().roots()); rr=np.real(roots[np.abs(np.imag(roots))<1e-8]) if roots.size else np.array([])
    xl=np.r_[-1.,A,rr[(rr>=-1)&(rr<=A)]]; xr=np.r_[A,1.,rr[(rr>=A)&(rr<=1)]]
    minL=float(np.min(p(xl))); minR=float(np.min(p(xr)-1.0))
    return float(val),{'status':prob.status,'min_left':minL,'min_right_minus1':minR,'max_abs_c':float(np.max(np.abs(cv)))}


def main():
    tp=hf_hub_download('Dingdong-Inc/FreshRetailNet-50K','data/train.parquet',repo_type='dataset')
    tr=pd.read_parquet(tp,columns=['store_id','product_id','dt','stock_hour6_22_cnt']); tr['event']=(tr.stock_hour6_22_cnt>0).astype(np.uint8); tr=tr.sort_values(['store_id','product_id','dt'])
    N=tr[['store_id','product_id']].drop_duplicates().shape[0]; X=tr.event.to_numpy().reshape(N,90); x=2*X.mean(1)-1
    installed=cp.installed_solvers(); solvers=[s for s in ['CLARABEL','CVXOPT','SCS'] if s in installed]; print('solvers',solvers,flush=True)
    rows=[]
    for n in DEPTHS:
        m=np.mean(C.chebvander(x,n),axis=0); row={'depth':n}
        for s in solvers:
            try:
                val,diag=solve(m,n,s); row[s.lower()+'_upper']=val; row[s.lower()+'_status']=diag['status']; row[s.lower()+'_min_left']=diag['min_left']; row[s.lower()+'_min_right_minus1']=diag['min_right_minus1']; row[s.lower()+'_max_abs_c']=diag['max_abs_c']
            except Exception as e: row[s.lower()+'_error']=repr(e)
        rows.append(row); print(row,flush=True)
    df=pd.DataFrame(rows); df.to_csv(OUT/'freshretail_sos_cheb_bounds.csv',index=False)
    audit={'series':int(N),'alpha':ALPHA,'installed_solvers':installed}
    for s in solvers:
        col=s.lower()+'_upper'
        if col in df:
            z=pd.to_numeric(df[col],errors='coerce').dropna().to_numpy(); audit[s+'_monotone_nonincreasing']=bool(np.all(np.diff(z)<=1e-6))
    (OUT/'audit.json').write_text(json.dumps(audit,indent=2)); print(json.dumps(audit,indent=2))

if __name__=='__main__':main()
