# Invalid records storage

import os 
from config import out_path

def rejected_data(df):
    try:
        inavlid_df=df[df['total_amount_usd']<0]
        os.makedirs(out_path,exist_ok=True)
        inavlid_df.to_csv(os.path.join(out_path,'rejected_data.csv'),index=False)
        print("Rejected records stored Successfully")
    except Exception as e:
        print("Error while Stroing Invalid Records{}".format(e))
        raise