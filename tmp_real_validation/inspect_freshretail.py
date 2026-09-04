from huggingface_hub import HfApi, hf_hub_download
import pyarrow.parquet as pq, json, pandas as pd
api=HfApi()
files=api.list_repo_files('Dingdong-Inc/FreshRetailNet-50K', repo_type='dataset')
print('FILES', files)
for f in files:
    if f.endswith('.parquet'):
        try:
            p=hf_hub_download('Dingdong-Inc/FreshRetailNet-50K',f,repo_type='dataset')
            pf=pq.ParquetFile(p)
            print('PARQUET',f,'rows',pf.metadata.num_rows,'schema',pf.schema_arrow)
            df=pd.read_parquet(p).head(3)
            print(df.to_json(orient='records',force_ascii=False))
        except Exception as e:
            print('ERR',f,repr(e))
