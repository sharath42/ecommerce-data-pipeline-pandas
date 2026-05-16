import os
from config import out_path
from datetime import datetime
def save_file(df):
    try:
        current_date = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = ('processed_data{}.csv'.format(current_date))
        os.makedirs(out_path, exist_ok=True)
        df.to_csv(os.path.join(out_path, filename), index=False)
        print("Data saved Successfully")
    except Exception as e:
        print("Error saving data: {}".format(e))
        raise