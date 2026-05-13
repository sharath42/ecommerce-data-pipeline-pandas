# Aggreation and group by

def data_cal(df):
    try:
        df['tota_per_customer']=df.groupby('customer_id').agg({'total_amount_inr':'sum'})
        df = df.sort_values(by='country',ascending=False)
        print("Calculated part is sucessfully completed")
        return df
    except Exception as e:
        print("Error while calculating{}".format(e))
        raise
