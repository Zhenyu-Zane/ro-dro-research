#!/usr/bin/env python3
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import linprog
from scipy.stats import binom
from numpy.polynomial import chebyshev as C
from huggingface_hub import hf_hub_download

OUT=Path('solver_repair_output'); OUT.mkdir(exist_ok=True)
ALPHA=.60
DEPTHS=[2,4,6,8,12,16,24,32]


def bern_eval(coeff, v):
    coeff=np.asarray(coeff,float); v=np.asarray(v,float); n=len(coeff)-1
    B=np.vstack([binom.pmf(k,n,v) for k in range(n+1)])
    return np.tensordot(coeff,B,axes=(0,0))


def bern_min_stable(coeff,left,right):
    coeff=np.asarray(coeff,float); n=len(coeff)-1
    if n==0:
        return float(coeff[0]), float(left)
    # Re-express the same polynomial in a Chebyshev basis by stable interpolation
    # at first-kind Chebyshev nodes, then locate every derivative root. Candidate
    # values are evaluated back in the original Bernstein basis.
    tc=C.chebinterpolate(lambda x: bern_eval(coeff,(np.asarray(x)+1.0)/2.0),n)
    poly=C.Chebyshev(tc)
    roots=np.asarray(poly.deriv().roots())
    rr=np.real(roots[np.abs(np.imag(roots))<1e-9]) if roots.size else np.array([])
    xlo,xhi=2*left-1,2*right-1
    rr=rr[(rr>=xlo-1e-10)&(rr<=xhi+1e-10)]
    xs=np.r_[xlo,xhi,rr]
    vs=(xs+1)/2
    vals=np.asarray(bern_eval(coeff,vs),float)
    j=int(np.argmin(vals))
    # independent dense-grid guard against root-finding loss
    vg=np.linspace(left,right,20001)
    qg=np.asarray(bern_eval(coeff,vg),float)
    jg=int(np.argmin(qg))
    if qg[jg] < vals[j]-1e-8:
        return float(qg[jg]), float(vg[jg])
    return float(vals[j]), float(vs[j])


def bernstein_upper(pk,alpha,tol=5e-10,maxiter=100):
    p=np.asarray(pk,float); p=p/p.sum(); n=len(p)-1
    grid=np.unique(np.r_[np.linspace(0,1,1201),alpha])
    last=None
    for it in range(maxiter):
        B=np.vstack([binom.pmf(k,n,grid) for k in range(n+1)])
        h=(grid>=alpha).astype(float)
        res=linprog(p,A_ub=-B.T,b_ub=-h,bounds=[(None,None)]*(n+1),method='highs')
        if not res.success: raise RuntimeError(f'Bernstein dual n={n}: {res.message}')
        d=np.asarray(res.x,float)
        m0,x0=bern_min_stable(d,0.,alpha)
        m1,x1=bern_min_stable(d,alpha,1.)
        v0=max(0.,-m0); v1=max(0.,1.-m1); worst=max(v0,v1)
        last=(res,d,m0,x0,m1,x1)
        if worst<=tol:
            corr=worst
            return float(res.fun+corr),d,{'iterations':it+1,'raw_objective':float(res.fun),'correction':float(corr),'min_left':m0,'argmin_left':x0,'min_right':m1,'argmin_right':x1,'max_abs_coeff':float(np.max(np.abs(d)))}
        add=[]
        if v0>tol: add.append(x0)
        if v1>tol: add.append(x1)
        grid=np.unique(np.r_[grid,add])
    res,d,m0,x0,m1,x1=last
    corr=max(0.,-m0,1.-m1)
    return float(res.fun+corr),d,{'iterations':maxiter,'raw_objective':float(res.fun),'correction':float(corr),'min_left':m0,'argmin_left':x0,'min_right':m1,'argmin_right':x1,'max_abs_coeff':float(np.max(np.abs(d))),'warning':'maxiter'}


def cheb_min(coeff,left,right):
    p=C.Chebyshev(np.asarray(coeff,float)); roots=np.asarray(p.deriv().roots())
    rr=np.real(roots[np.abs(np.imag(roots))<1e-9]) if roots.size else np.array([])
    rr=rr[(rr>=left-1e-10)&(rr<=right+1e-10)]
    xs=np.r_[left,right,rr]; vals=np.asarray(p(xs),float); j=int(np.argmin(vals))
    return float(vals[j]),float(xs[j])


def chebyshev_upper(full_rate,n,alpha,tol=5e-10,maxiter=100):
    x=2*np.asarray(full_rate,float)-1
    moments=np.mean(C.chebvander(x,n),axis=0)
    a=2*alpha-1
    grid=np.unique(np.r_[np.linspace(-1,1,1201),a])
    last=None
    for it in range(maxiter):
        V=C.chebvander(grid,n); h=(grid>=a).astype(float)
        res=linprog(moments,A_ub=-V,b_ub=-h,bounds=[(None,None)]*(n+1),method='highs')
        if not res.success: raise RuntimeError(f'Chebyshev dual n={n}: {res.message}')
        c=np.asarray(res.x,float)
        m0,x0=cheb_min(c,-1.,a); m1,x1=cheb_min(c,a,1.)
        v0=max(0.,-m0); v1=max(0.,1.-m1); worst=max(v0,v1)
        last=(res,c,m0,x0,m1,x1)
        if worst<=tol:
            return float(res.fun+worst),c,{'iterations':it+1,'raw_objective':float(res.fun),'correction':float(worst),'min_left':m0,'min_right':m1,'max_abs_coeff':float(np.max(np.abs(c)))}
        add=[]
        if v0>tol:add.append(x0)
        if v1>tol:add.append(x1)
        grid=np.unique(np.r_[grid,add])
    res,c,m0,x0,m1,x1=last; corr=max(0.,-m0,1.-m1)
    return float(res.fun+corr),c,{'iterations':maxiter,'raw_objective':float(res.fun),'correction':float(corr),'min_left':m0,'min_right':m1,'max_abs_coeff':float(np.max(np.abs(c))),'warning':'maxiter'}


def primal_grid_lower(pk,n,alpha,full_rate,dual_bern_coeff):
    # Include the exact empirical support (multiples of 1/90), a dense grid, and
    # all near-contact points of the final dual. This is a lower bound because
    # the primal support is restricted, while the dual upper is continuous-domain.
    support=np.unique(np.r_[np.unique(full_rate),np.linspace(0,1,4001),alpha])
    q=np.asarray(bern_eval(dual_bern_coeff,support),float)
    h=(support>=alpha).astype(float)
    contact=support[(q-h)<=2e-5]
    support=np.unique(np.r_[support,contact])
    B=np.vstack([binom.pmf(k,n,support) for k in range(n+1)])
    res=linprog(-h,A_eq=B,b_eq=np.asarray(pk,float),bounds=[(0,None)]*len(support),method='highs')
    if not res.success:
        # equality presolve can be sensitive; retry after dropping the redundant last row
        res=linprog(-h,A_eq=B[:-1],b_eq=np.asarray(pk,float)[:-1],bounds=[(0,None)]*len(support),method='highs')
    if not res.success: raise RuntimeError(f'Primal lower n={n}: {res.message}')
    return float(-res.fun),{'support_size':int(len(support)),'eq_max_resid':float(np.max(np.abs(B@res.x-np.asarray(pk,float))))}


def main():
    tp=hf_hub_download('Dingdong-Inc/FreshRetailNet-50K','data/train.parquet',repo_type='dataset')
    tr=pd.read_parquet(tp,columns=['store_id','product_id','dt','stock_hour6_22_cnt'])
    tr['event']=(tr.stock_hour6_22_cnt>0).astype(np.uint8)
    tr=tr.sort_values(['store_id','product_id','dt'])
    N=tr[['store_id','product_id']].drop_duplicates().shape[0]
    X=tr.event.to_numpy().reshape(N,90); full_rate=X.mean(1)
    rows=[]
    for n in DEPTHS:
        pk=np.array([np.mean(binom.pmf(k,n,full_rate)) for k in range(n+1)])
        bu,bd,bdiag=bernstein_upper(pk,ALPHA)
        cu,cd,cdiag=chebyshev_upper(full_rate,n,ALPHA)
        pl,pdiag=primal_grid_lower(pk,n,ALPHA,full_rate,bd)
        row={'depth':n,'bernstein_upper':bu,'chebyshev_upper':cu,'primal_grid_lower':pl,
             'bern_cheb_abs_diff':abs(bu-cu),'upper_lower_gap':min(bu,cu)-pl,
             'bern_iterations':bdiag['iterations'],'bern_correction':bdiag['correction'],'bern_max_abs_coeff':bdiag['max_abs_coeff'],
             'cheb_iterations':cdiag['iterations'],'cheb_correction':cdiag['correction'],'cheb_max_abs_coeff':cdiag['max_abs_coeff'],
             'primal_eq_max_resid':pdiag['eq_max_resid']}
        rows.append(row); print(row,flush=True)
    out=pd.DataFrame(rows); out.to_csv(OUT/'freshretail_solver_repair.csv',index=False)
    vals=out['chebyshev_upper'].to_numpy()
    mono=bool(np.all(np.diff(vals)<=1e-7))
    audit={'series':int(N),'alpha':ALPHA,'depths':DEPTHS,'chebyshev_monotone_nonincreasing':mono,
           'max_parameterization_difference':float(out.bern_cheb_abs_diff.max()),
           'max_primal_dual_gap':float(out.upper_lower_gap.max())}
    (OUT/'freshretail_solver_repair_audit.json').write_text(json.dumps(audit,indent=2))
    print(json.dumps(audit,indent=2))

if __name__=='__main__': main()
