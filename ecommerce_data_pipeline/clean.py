# Data clean 
import pandas as pd

def data_clean(df):
    try:
        # Remove duplicate rows
        df=df.drop_duplicates()
        # Remove duplicate order ids keep latest
        if'order_date' in df.columns:
            df['order_date']=pd.to_datetime(df['order_date'])
            df.sort_values('order_date')
            df=df.drop_duplicates(subset='order_id',keep='last')

        # Remove Null Values
        df=df.fillna({
        'discount_amount_usd': 0,
        'shipping_fee_usd': 0,
        'tax_amount_usd': 0},inplace=True)

        #Remove Inavlid Age 
        if 'age' in df.columns:
            df=df[df['age']>=18]

        # Remove invalid email
        if 'email' in df.columns:
            df=df[df['email'].str.contains('@',na=False)]

        # Standardize the text columns
        if 'country' in df.columns:
            df['country']=df['country'].str.upper()
        print("Data is Cleaned Successfully Completed")
        return df
    except Exception as e:
        print("Error While Cleaning {}".format(e))
        raise