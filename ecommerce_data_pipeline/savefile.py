# cleaned data is stored path

import os
from config import out_path
from datetime import datetime

def output(df):
    try:
        current_date=datetime.now().strftime('%Y%m%d_%H%M%S')
        file_path=('final_data_{}.csv'.format(current_date))
        os.makedirs(out_path,exist_ok=True)
        df.to_csv(os.path.join(out_path,file_path),index=False)
        print("Data is Successfully Loaded and Transformed")
    except Exception as e:
        print("Error While Saving the final data{}".format(e))
        raise

