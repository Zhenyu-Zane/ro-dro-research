from huggingface_hub import hf_hub_download
import pandas as pd, numpy as np, json
from pathlib import Path
out=Path('real_validation_output'); out.mkdir(exist_ok=True)
tr=hf_hub_download('Dingdong-Inc/FreshRetailNet-50K','data/train.parquet',repo_type='dataset')
ev=hf_hub_download('Dingdong-Inc/FreshRetailNet-50K','data/eval.parquet',repo_type='dataset')
cols=['store_id','product_id','stock_hour6_22_cnt']
a=pd.read_parquet(tr,columns=cols); b=pd.read_parquet(ev,columns=cols)
for d in (a,b): d['event']=(d.stock_hour6_22_cnt>0).astype(int)
g=a.groupby(['store_id','product_id']).event.agg(['mean','count'])
h=b.groupby(['store_id','product_id']).event.agg(['mean','count'])
idx=g.index.intersection(h.index); g=g.loc[idx]; h=h.loc[idx]
profile={'train_rows':len(a),'eval_rows':len(b),'series_common':len(idx),'train_count_min':int(g['count'].min()),'train_count_max':int(g['count'].max()),'eval_count_min':int(h['count'].min()),'eval_count_max':int(h['count'].max()),'train_event_mean':float(a.event.mean()),'eval_event_mean':float(b.event.mean()),'train_rate_quantiles':{str(q):float(g['mean'].quantile(q)) for q in [0,.1,.25,.5,.75,.9,.95,.99,1]},'eval_rate_quantiles':{str(q):float(h['mean'].quantile(q)) for q in [0,.1,.25,.5,.75,.9,.95,.99,1]},'tail_fractions_train':{str(x):float(np.mean(g['mean']>=x)) for x in [.1,.2,.3,.4,.5,.6,.7,.8]},'tail_fractions_eval':{str(x):float(np.mean(h['mean']>=x)) for x in [.1,.2,.3,.4,.5,.6,.7,.8]}}
(out/'freshretail_stockout_profile.json').write_text(json.dumps(profile,indent=2)); print(json.dumps(profile,indent=2))
