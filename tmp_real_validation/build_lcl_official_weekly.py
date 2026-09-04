#!/usr/bin/env python3
from pathlib import Path
import requests, zipfile, pandas as pd, numpy as np, json, time
URL='https://data.london.gov.uk/download/smartmeter-energy-use-data-in-london-households/04feba67-f1a3-4563-98d0-f3071e3d56d1/Partitioned%20LCL%20Data.zip'
out=Path('real_validation_output'); out.mkdir(exist_ok=True)
zpath=Path('/tmp/lcl.zip')
t=time.time()
with requests.get(URL,stream=True,timeout=120) as r:
    r.raise_for_status()
    with zpath.open('wb') as f:
        for ch in r.iter_content(8*1024*1024):
            if ch:f.write(ch)
print('downloaded',zpath.stat().st_size)
agg=[]; rows=0; kept=0
with zipfile.ZipFile(zpath) as z:
    names=[n for n in z.namelist() if n.lower().endswith('.csv')]
    print('members',len(names),names[:3])
    for j,nm in enumerate(names):
        with z.open(nm) as fh:
            for df in pd.read_csv(fh,chunksize=300000):
                rows += len(df)
                # normalize likely column names
                cols={c.strip():c for c in df.columns}
                idc=next(c for c in df.columns if c.strip().lower()=='lclid')
                tc=next(c for c in df.columns if 'datetime' in c.strip().lower())
                kc=next(c for c in df.columns if 'kwh' in c.strip().lower())
                tariff=next((c for c in df.columns if 'stdortou' in c.strip().lower()),None)
                s=df[tc].astype(str)
                mask=s.str.startswith('2013-')
                if tariff is not None: mask &= df[tariff].astype(str).str.lower().eq('std')
                d=df.loc[mask,[idc,tc,kc]].copy(); kept+=len(d)
                if d.empty: continue
                d[kc]=pd.to_numeric(d[kc],errors='coerce')
                d=d.dropna(subset=[kc])
                dt=pd.to_datetime(d[tc],errors='coerce')
                d=d.loc[dt.notna()].copy(); dt=dt[dt.notna()]
                # Monday-start week using period; store start date
                d['week']=dt.dt.to_period('W-SUN').dt.start_time
                g=d.groupby([idc,'week'],as_index=False)[kc].sum()
                agg.append(g)
        if (j+1)%20==0: print('done',j+1,'rows',rows,'kept',kept,'elapsed',time.time()-t)
allg=pd.concat(agg,ignore_index=True)
idc=allg.columns[0]; kc=allg.columns[-1]
allg=allg.groupby([idc,'week'],as_index=False)[kc].sum()
wide=allg.pivot(index=idc,columns='week',values=kc).sort_index(axis=1)
# Require at least 50 valid weeks in 2013; fill only <=3 missing weeks by within-household median.
good=wide.notna().sum(axis=1)>=50; wide=wide.loc[good]
missing=int(wide.isna().sum().sum()); wide=wide.T.fillna(wide.median(axis=1)).T
wide.to_csv(out/'lcl_official_std_2013_weekly.csv')
meta={'source_url':URL,'raw_rows_read':rows,'rows_std_2013':kept,'households':len(wide),'weeks':wide.shape[1],'missing_week_cells_imputed':missing,'filter':'Std tariff, calendar year 2013, >=50 observed weekly totals','download_bytes':zpath.stat().st_size,'elapsed_sec':time.time()-t}
(out/'lcl_official_build_meta.json').write_text(json.dumps(meta,indent=2,default=str));print(json.dumps(meta,indent=2,default=str))
