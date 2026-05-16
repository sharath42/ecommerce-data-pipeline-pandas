# Ingestion script for loading and preprocessing loan data

import pandas as pd
from config import data_path
import os

def load_data():
    try:
        cus_df=pd.read_csv(os.path.join(data_path, 'customers.csv'))
        loan_df=pd.read_csv(os.path.join(data_path, 'loans.csv'))
        return cus_df, loan_df
    except Exception as e:
        print("Error loading data: {}".format(e))
        raise