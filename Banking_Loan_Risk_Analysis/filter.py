# Filtering the Data sets
from config import Loan_status
def filter_data(df,Loan_status):
    try:
        filter_df=df[df['status'].isin(Loan_status)]
        print("Data filtered Successfully for {}".format(Loan_status))
        return filter_df
    except Exception as e:
        print("Error filtering data: {}".format(e))
        raise