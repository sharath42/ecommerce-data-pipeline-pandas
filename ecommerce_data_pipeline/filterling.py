# Filtering the data

from config import category_list,year_list

def filter_data(df,category_list,year_list):
    try:
        filter_data=df[(df['category'].isin(category_list))& (df['year'].isin(year_list))]
        print("Data Filtering is Done Successfully under{} categories and {} years".format(category_list,year_list))
        return filter_data
    except Exception as e:
        print("Error while filtering the Data{}".format(e))
