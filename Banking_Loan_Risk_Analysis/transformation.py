import pandas as pd

def trans_data(df):

    try:

        # Convert application_date to datetime
        df['application_date'] = pd.to_datetime(
            df['application_date'],
            errors='coerce'
        )

        # Extract year
        df['application_year'] = (
            df['application_date']
            .dt.year
        )

        # Monthly interest rate
        df['monthly_interest_rate'] = (
            df['interest_rate'] / 12
        )

        # Loan months
        df['loan_months'] = (
            df['loan_years'] * 12
        )

        # EMI Calculation
        P = df['loan_amount']

        R = (
            df['monthly_interest_rate'] / 100
        )

        N = df['loan_months']

        df['emi'] = (
            (P * R * (1 + R) ** N)
            /
            (((1 + R) ** N) - 1)
        )

        # Loan reference id
        df['loan_ref_id'] = (
            'Loan_'
            +
            df['application_year']
            .astype(str)
            +
            '_'
            +
            df['loan_id']
            .astype(str)
        )

        print(
            "Data Transformed Successfully"
        )

        return df

    except Exception as e:

        print(
            "Error transforming data: {}"
            .format(e)
        )

        raise