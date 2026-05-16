import os
from datetime import datetime
from config import out_path

def rejected_data(df):
    try:
        current_date=datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path=('rejected_data_{}.csv'.format(current_date))
        invalid_df=df[(df['loan_amount']<0)&(df['status']=='Rejected')]
        os.makedirs(out_path,exist_ok=True)
        invalid_df.to_csv(os.path.join(out_path,file_path),index=False)
        print("Rejected records stored Successfully")
    except Exception as e:
        print("Error while Stroing Invalid Records{}".format(e))
        raise