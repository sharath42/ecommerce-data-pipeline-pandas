#Transforming the data according to business logic
from logging import exception

from config import usd_to_inr_rate

def tran_data(df,usd_to_inr_rate):
    try:
        # Currency conversion
        df['subtotal_inr'] = df['subtotal_usd']*usd_to_inr_rate
        df['discount_amount_inr'] = df['discount_amount_usd']*usd_to_inr_rate
        df['shipping_fee_inr'] = df['shipping_fee_usd']*usd_to_inr_rate
        df['tax_amount_inr'] = df['tax_amount_usd']*usd_to_inr_rate
        df['total_amount_inr'] = df['total_amount_usd']*usd_to_inr_rate
        df['total_amount_inr']=df['total_amount_inr'].round(2)
        df['net_amount']=(df['total_amount_inr']-df['discount_amount_inr']-df['tax_amount_inr'])
        print('USD to INR currency conversion columns are inserted')
        # Create Unique Bussiness id
        df['Ele_id'] = 'E' + df['year'].astype(str)
        return df
    except exception as e:
        print("Error While Transforming{}".format(e))
        raise