# Merge or Joining the Data sets

def merge_data(cus_df, loan_df):
    try:
        df = cus_df.merge(loan_df, on='customer_id', how='inner')
        return df
    except Exception as e:
        print("Error merging data: {}".format(e))
        raise