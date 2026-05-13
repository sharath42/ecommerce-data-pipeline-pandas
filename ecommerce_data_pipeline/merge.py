# Merge or Joining the Data sets

def merge_data(cus_df,ord_df):
    try:    
        df=cus_df.merge(ord_df, on='customer_id',how='inner')
        print('Data Successfully Joined')
        return df
    except Exception as e:
        print("Error While Joining the Data Sets{}".format(e))
        raise