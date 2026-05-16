# cleaning the Data sets
import pandas as pd
def clean_data(df):
    try:
        # Remove duplicate rows
        df=df.drop_duplicates()
        # Convert loan_amount to numeric and handle errors
        df['loan_amount'] = pd.to_numeric(df['loan_amount'], errors='coerce')
        # Strip whitespace from loan_status
        df['status'] = df['status'].str.strip()
        # Remove duplicate loan ids keep latest
        df=df.drop_duplicates(subset=['loan_id'],keep='last')
        # Remove Null Values
        df=df.fillna({
            'loan_amount': 0,
            'status': 'Unknown'
        })
        # Remove invalid age
        if 'age' in df.columns:
            df=df[df['age'] >= 18]
        # Remove invalid email
        if 'email' in df.columns:
            df=df[df['email'].str.contains('@',na=False)]
        # Standardize the text columns
        if 'city' in df.columns:
            df['city']=df['city'].str.upper()
        if 'state' in df.columns:
            df['state']=df['state'].str.upper()
        if 'loan_type' in df.columns:
            df['loan_type']=df['loan_type'].str.upper()      
        print("Data cleaned Successfully")
        return df
    except Exception as e:
        print("Error cleaning data: {}".format(e))
        raise