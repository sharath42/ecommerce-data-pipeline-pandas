#Reading data from source files

import pandas as pd
import os
from config import data_path

def load_data():
    try:

        cus_df=pd.read_csv(os.path.join(data_path,'customers.csv'))
        ord_df=pd.read_csv(os.path.join(data_path,'orders.csv'))
        print("Data is Loaded Successfully")
        return cus_df,ord_df
    except Exception as e:
        print("Error while loading the data{}".format(e))
        raise