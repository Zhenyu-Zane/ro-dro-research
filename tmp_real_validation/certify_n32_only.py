#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import pandas as pd
import mpmath as mp
from scipy.optimize import linprog
from numpy.polynomial import chebyshev as C
from huggingface_hub import hf_hub_download

OUT=Path('n32_cert_output'); OUT.mkdir(exist_ok=True)
NDEG=32; ALPHA=.60; AX=2*ALPHA-1


def cheb_min(c,l,u):
    p=C.Chebyshev(c); r=np.asarray(p.deriv().roots()); rr=np.real(r[np.abs(np.imag(r))<1e-8]) if r.size else np.array([]); rr=rr[(rr>=l)&(rr<=u)]
    x=np.r_[l,u,rr]; y=p(x); j=int(np.argmin(y)); return float(y[j]),float(x[j]),rr

def adaptive(m,maxiter=100):
    grid=np.unique(np.r_[np.linspace(-1,1,1201),AX]); last=None
    for it in range(maxiter):
        V=C.chebvander(grid,NDEG); h=(grid>=AX).astype(float)
        res=linprog(m,A_ub=-V,b_ub=-h,bounds=[(None,None)]*(NDEG+1),method='highs')
        if not res.success: raise RuntimeError(f'iter {it}: {res.message}')
        c=np.asarray(res.x,float); ml,xl,_=cheb_min(c,-1,AX); mr,xr,_=cheb_min(c,AX,1); vl=max(0,-ml); vr=max(0,1-mr); last=(res,c,ml,mr,xl,xr)
        add=[]
        if vl>1e-10:add.append(xl)
        if vr>1e-10:add.append(xr)
        if not add: break
        grid=np.unique(np.r_[grid,add])
    return last,grid

def cheb_to_power(c):
    mp.mp.dps=100; n=len(c)-1; polys=[[mp.mpf(1)]]
    if n>=1:polys.append([mp.mpf(0),mp.mpf(1)])
    for k in range(1,n):
        p=polys[-1]; q=polys[-2]; xp=[mp.mpf(0)]+[2*z for z in p]; q=q+[mp.mpf(0)]*(len(xp)-len(q)); polys.append([xp[i]-q[i] for i in range(len(xp))])
    out=[mp.mpf(0)]*(n+1)
    for k,ck in enumerate(c):
        cc=mp.mpf(repr(float(ck)))
        for j,z in enumerate(polys[k]):out[j]+=cc*z
    return out

def restrict(power,l,u,subtract=0):
    n=len(power)-1; a=[mp.mpf(0)]*(n+1); L=mp.mpf(str(l)); W=mp.mpf(str(u))-L
    power=list(power); power[0]-=mp.mpf(str(subtract))
    for j,z in enumerate(power):
        for r in range(j+1):a[r]+=z*mp.binomial(j,r)*(L**(j-r))*(W**r)
    return a

def p2b(a):
    n=len(a)-1; b=[]
    for k in range(n+1):b.append(sum(a[j]*mp.binomial(k,j)/mp.binomial(n,j) for j in range(k+1)))
    return b

def split(b):
    tri=[list(b)]; n=len(b)-1
    for r in range(1,n+1):tri.append([(tri[r-1][i]+tri[r-1][i+1])/2 for i in range(n-r+1)])
    return [tri[r][0] for r in range(n+1)],[tri[n-r][r] for r in range(n+1)]

def lower_bound(c,l,u,subtract,depth=14):
    b=p2b(restrict(cheb_to_power(c),l,u,subtract)); cells=[b]
    for _ in range(depth):
        nxt=[]
        for z in cells:
            a,b2=split(z); nxt.extend([a,b2])
        cells=nxt
    return float(min(min(z) for z in cells))

def primal(m,c):
    p=C.Chebyshev(c); roots=np.asarray(p.deriv().roots()); rr=np.real(roots[np.abs(np.imag(roots))<1e-8]) if roots.size else np.array([]); rr=rr[(rr>=-1)&(rr<=1)]
    support=np.unique(np.r_[np.linspace(-1,1,16001),rr,AX]); A=C.chebvander(support,NDEG).T; h=(support>=AX).astype(float)
    res=linprog(-h,A_eq=A,b_eq=m,bounds=[(0,None)]*len(support),method='highs')
    if not res.success:raise RuntimeError(res.message)
    return float(-res.fun),float(np.max(np.abs(A@res.x-m)))

def main():
    tp=hf_hub_download('Dingdong-Inc/FreshRetailNet-50K','data/train.parquet',repo_type='dataset'); tr=pd.read_parquet(tp,columns=['store_id','product_id','dt','stock_hour6_22_cnt']); tr['event']=(tr.stock_hour6_22_cnt>0).astype(np.uint8); tr=tr.sort_values(['store_id','product_id','dt']); N=tr[['store_id','product_id']].drop_duplicates().shape[0]; X=tr.event.to_numpy().reshape(N,90); x=2*X.mean(1)-1
    m=np.mean(C.chebvander(x,NDEG),axis=0); (res,c,ml,mr,xl,xr),grid=adaptive(m,100)
    L=lower_bound(c,-1,AX,0,14); R=lower_bound(c,AX,1,1,14); corr=max(0,-L,-R); upper=float(res.fun+corr); pl,pr=primal(m,c)
    out={'depth':32,'raw_dual':float(res.fun),'certified_upper':upper,'cert_correction':corr,'left_cert_lb':L,'right_cert_lb':R,'float_min_left':ml,'float_min_right':mr,'grid_size':len(grid),'max_abs_cheb_coeff':float(np.max(np.abs(c))),'primal_grid_lower':pl,'primal_residual':pr,'gap':upper-pl,'series':int(N)}
    (OUT/'n32_certified.json').write_text(json.dumps(out,indent=2)); pd.DataFrame([out]).to_csv(OUT/'n32_certified.csv',index=False); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
