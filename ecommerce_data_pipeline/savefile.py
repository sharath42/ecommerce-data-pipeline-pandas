# cleaned data is stored path

import os
from config import out_path

def output(df):
    try:
        os.makedirs(out_path,exist_ok=True)
        df.to_csv(os.path.join(out_path,'final_data.csv'),index=False)
        print("Data is Successfully Loaded and Transformed")
    except Exception as e:
        print("Error While Saving the final data{}".format(e))
        raise

