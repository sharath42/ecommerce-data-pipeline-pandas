#Main pipeline 

from ingestion import load_data
from merge import merge_data
from filterling import filter_data
from clean import data_clean
from transform import tran_data
from cal import data_cal
from validation import rejected_data
from savefile import output
from config import category_list, year_list, usd_to_inr_rate





def pipeline():
    try:
        cust_df,ord_df =load_data()
        merging_data = merge_data(cust_df,ord_df)
        rejected=rejected_data(merging_data)
        filter_data2 = filter_data(merging_data,category_list,year_list)
        cleaned_data = data_clean(filter_data2)
        conv_data = tran_data(cleaned_data,usd_to_inr_rate)
        cal_part = data_cal(conv_data)
        saving_data = output(cal_part)
        print('Pipeline excuted sucessfully')
    except Exception as e:
        print("Pipeline Failed{}".format(e))


#Entry point
if __name__ =='__main__':
    pipeline()