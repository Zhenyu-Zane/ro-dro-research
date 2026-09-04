#!/usr/bin/env python3
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
import pandas as pd
import mpmath as mp
from scipy.optimize import linprog
from numpy.polynomial import chebyshev as C
from huggingface_hub import hf_hub_download

OUT=Path('certified_bound_output'); OUT.mkdir(exist_ok=True)
DEPTHS=[2,4,6,8,12,16,24,32]
ALPHA=.60; AX=2*ALPHA-1


def cheb_min_float(c,left,right):
    p=C.Chebyshev(np.asarray(c,float)); roots=np.asarray(p.deriv().roots())
    rr=np.real(roots[np.abs(np.imag(roots))<1e-8]) if roots.size else np.array([])
    rr=rr[(rr>=left-1e-10)&(rr<=right+1e-10)]
    xs=np.r_[left,right,rr]; vals=np.asarray(p(xs),float); j=int(np.argmin(vals))
    return float(vals[j]),float(xs[j]),rr


def adaptive_cheb_upper(m,n,alpha_x,tol=1e-10,maxiter=300):
    grid=np.unique(np.r_[np.linspace(-1,1,1601),alpha_x])
    last=None
    for it in range(maxiter):
        V=C.chebvander(grid,n); h=(grid>=alpha_x).astype(float)
        res=linprog(m,A_ub=-V,b_ub=-h,bounds=[(None,None)]*(n+1),method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
        if not res.success: raise RuntimeError(res.message)
        c=np.asarray(res.x,float)
        ml,xl,_=cheb_min_float(c,-1,alpha_x); mr,xr,_=cheb_min_float(c,alpha_x,1)
        vl=max(0.,-ml); vr=max(0.,1-mr); worst=max(vl,vr); last=(res,c,ml,xl,mr,xr)
        if worst<=tol: break
        add=[]
        if vl>tol:add.append(xl)
        if vr>tol:add.append(xr)
        grid=np.unique(np.r_[grid,add])
    res,c,ml,xl,mr,xr=last
    return float(res.fun),c,{'iterations':it+1,'float_min_left':ml,'float_min_right':mr,'grid_size':len(grid)}


def cheb_to_power_mp(c):
    mp.mp.dps=90; n=len(c)-1
    # polynomial coefficients low-to-high
    T0=[mp.mpf(1)]; polys=[T0]
    if n>=1: polys.append([mp.mpf(0),mp.mpf(1)])
    for k in range(1,n):
        prev=polys[-1]; prev2=polys[-2]
        xprev=[mp.mpf(0)]+[2*z for z in prev]
        if len(prev2)<len(xprev): prev2=prev2+[mp.mpf(0)]*(len(xprev)-len(prev2))
        polys.append([xprev[i]-prev2[i] for i in range(len(xprev))])
    out=[mp.mpf(0)]*(n+1)
    for k,ck in enumerate(c):
        for j,a in enumerate(polys[k]): out[j]+=mp.mpf(repr(float(ck)))*a
    return out


def restrict_power_to_unit(power,l,u):
    # x=l+(u-l)t
    n=len(power)-1; out=[mp.mpf(0)]*(n+1); w=mp.mpf(u)-mp.mpf(l); lm=mp.mpf(l)
    for j,aj in enumerate(power):
        for r in range(j+1): out[r]+=aj*mp.binomial(j,r)*(lm**(j-r))*(w**r)
    return out


def power_to_bern(a):
    n=len(a)-1; b=[mp.mpf(0)]*(n+1)
    for k in range(n+1):
        s=mp.mpf(0)
        for j in range(k+1): s += a[j]*mp.binomial(k,j)/mp.binomial(n,j)
        b[k]=s
    return b


def subdivide_bern(b,t=mp.mpf('0.5')):
    n=len(b)-1; tri=[list(b)]
    for r in range(1,n+1): tri.append([(1-t)*tri[r-1][i]+t*tri[r-1][i+1] for i in range(n-r+1)])
    left=[tri[r][0] for r in range(n+1)]; right=[tri[n-r][r] for r in range(n+1)]
    return left,right


def certified_lower_bound(c,l,u,subtract=0.0,depth=13):
    power=cheb_to_power_mp(c); power[0]-=mp.mpf(str(subtract))
    local=restrict_power_to_unit(power,l,u); b=power_to_bern(local)
    cells=[b]
    for _ in range(depth):
        nxt=[]
        for z in cells:
            L,R=subdivide_bern(z); nxt.extend([L,R])
        cells=nxt
    lower=min(min(z) for z in cells)
    return float(lower)


def primal_cheb_lower(m,n,alpha,dual_c):
    # Stable restricted-support primal in Chebyshev coordinates. The exact empirical
    # support makes the moment equations feasible; a dense grid plus dual contact
    # candidates allows the lower bound to approach the unrestricted optimum.
    p=C.Chebyshev(np.asarray(dual_c,float)); dp=p.deriv(); r=np.asarray(dp.roots()); rr=np.real(r[np.abs(np.imag(r))<1e-8]) if r.size else np.array([])
    contacts=rr[(rr>=-1)&(rr<=1)]
    support_x=np.unique(np.r_[np.linspace(-1,1,8001),contacts,AX])
    A=C.chebvander(support_x,n).T; h=(support_x>=AX).astype(float)
    res=linprog(-h,A_eq=A,b_eq=m,bounds=[(0,None)]*len(support_x),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    if not res.success: raise RuntimeError('primal '+res.message)
    resid=float(np.max(np.abs(A@res.x-m)))
    return float(-res.fun),resid


def main():
    tp=hf_hub_download('Dingdong-Inc/FreshRetailNet-50K','data/train.parquet',repo_type='dataset')
    tr=pd.read_parquet(tp,columns=['store_id','product_id','dt','stock_hour6_22_cnt']); tr['event']=(tr.stock_hour6_22_cnt>0).astype(np.uint8); tr=tr.sort_values(['store_id','product_id','dt'])
    N=tr[['store_id','product_id']].drop_duplicates().shape[0]; X=tr.event.to_numpy().reshape(N,90); x=2*X.mean(1)-1
    rows=[]
    for n in DEPTHS:
        m=np.mean(C.chebvander(x,n),axis=0)
        raw,c,diag=adaptive_cheb_upper(m,n,AX)
        lbL=certified_lower_bound(c,-1,AX,0.0,depth=13); lbR=certified_lower_bound(c,AX,1,1.0,depth=13)
        correction=max(0.,-lbL,-lbR); upper=raw+correction
        pl,resid=primal_cheb_lower(m,n,ALPHA,c)
        row={'depth':n,'certified_upper':upper,'raw_dual_objective':raw,'bernstein_subdivision_correction':correction,
             'certified_left_lower_bound':lbL,'certified_right_lower_bound':lbR,'primal_grid_lower':pl,'upper_lower_gap':upper-pl,
             'primal_moment_residual':resid,'iterations':diag['iterations'],'float_min_left':diag['float_min_left'],'float_min_right':diag['float_min_right'],'max_abs_cheb_coeff':float(np.max(np.abs(c)))}
        rows.append(row); print(row,flush=True)
    df=pd.DataFrame(rows); df.to_csv(OUT/'freshretail_certified_bounds.csv',index=False)
    vals=df.certified_upper.to_numpy(); audit={'series':int(N),'alpha':ALPHA,'monotone_nonincreasing':bool(np.all(np.diff(vals)<=1e-7)),
        'max_upper_lower_gap':float(df.upper_lower_gap.max()),'max_correction':float(df.bernstein_subdivision_correction.max()),
        'max_primal_moment_residual':float(df.primal_moment_residual.max())}
    (OUT/'audit.json').write_text(json.dumps(audit,indent=2)); print(json.dumps(audit,indent=2))

if __name__=='__main__':main()
