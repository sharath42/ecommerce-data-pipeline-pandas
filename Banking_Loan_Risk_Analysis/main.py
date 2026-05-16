from ingestion import load_data
from merge import merge_data
from filter import filter_data
from transformation import trans_data
from validation import rejected_data                                                                                                                            
from clean import clean_data
from validation import rejected_data
from savefile import save_file
from config import Loan_status
def main():
    try:
        cus_df, loan_df = load_data()
        merged_data = merge_data(cus_df, loan_df)
        rejected_data(merged_data)
        filtered_df = filter_data(merged_data,Loan_status)
        cleaned_df = clean_data(filtered_df)
        transform_data1=trans_data(cleaned_df)
        save_file1=save_file(transform_data1)
    except Exception as e:
        print("Error in main execution: {}".format(e))
        raise
if __name__=='__main__':
    main()