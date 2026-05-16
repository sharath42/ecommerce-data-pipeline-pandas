Banking Loan Risk Analysis Pipeline

Project Overview

This project is an end-to-end Banking Loan Risk Analysis Data Pipeline
developed using Python and Pandas.

The pipeline performs:

-   Data Ingestion
-   Data Validation
-   Data Cleaning
-   Data Filtering
-   Data Transformation
-   Rejected Data Handling
-   Final Processed Data Storage

The main goal of this project is to process raw banking loan application
data and generate clean, transformed datasets for analysis and reporting
purposes.

Project Architecture

Raw CSV Files ↓ Ingestion Layer ↓ Merge Data ↓ Validation Layer ↓
Filtering Layer ↓ Cleaning Layer ↓ Transformation Layer ↓ Save Final
Processed Data

Technologies Used

-   Python 3.13
-   Pandas
-   OS Module
-   Datetime Module
-   VS Code
-   Git & GitHub

Project Folder Structure

Banking_Loan_Risk_Analysis/

├── Raw/ 
├── customers.csv 
└── loans.csv 
├── cleaned_data/ 
├──ingestion.py 
├── merge.py 
├── filter.py 
├── clean.py 
├── validation.py
├── transformation.py 
├── savefile.py 
├── config.py 
├── main.py 
│└──README.md

Business Requirements

The bank wants to analyze loan applications and identify valid customers
for loan approval.

The system should:

-   Load customer and loan data
-   Merge datasets using customer ID
-   Remove invalid records
-   Filter only approved and pending loans
-   Clean null and duplicate values
-   Validate email and age
-   Transform application dates
-   Calculate EMI values
-   Generate unique loan reference IDs
-   Store rejected records separately
-   Save final cleaned dataset with timestamp

Features Implemented

1. Data Ingestion

Loads raw CSV files into Pandas DataFrames.

Files Used: - customers.csv - loans.csv

2. Data Merging

Merged customer and loan datasets using pd.merge()

3. Data Validation

Rejected records are stored separately for: - Negative loan amounts -
Invalid records

Rejected files are saved with current timestamp.

Example: rejected_data_20260516_125500.csv

4. Data Filtering

Filters only: [‘Approved’, ‘Pending’]

loan statuses.

5. Data Cleaning

Performed: - Duplicate removal - Null handling - Invalid email removal -
Invalid age removal - Standardized text columns - Converted columns to
uppercase

6. Data Transformation

Performed: - Datetime conversion - Extract application year - EMI
calculation - Loan months calculation - Unique Loan Reference ID
generation

EMI Formula: EMI = (P × R × (1+R)^N) / ((1+R)^N - 1)

Where: - P = Loan Amount - R = Monthly Interest Rate - N = Loan Months

How to Run the Project

Step 1: Clone Repository

git clone

Step 2: Navigate to Project

cd Banking_Loan_Risk_Analysis

Step 3: Install Pandas

pip install pandas

Step 4: Run Project

python main.py

Sample Output

Rejected records stored Successfully Data filtered Successfully Data
cleaned Successfully Data Transformed Successfully Data saved
Successfully

Output Files

Generated files: - Rejected Records CSV - Final Cleaned CSV

Files are stored with current timestamp.

Example: processed_data_20260516_130200.csv

Learning Outcomes

Through this project, I learned:

-   End-to-End Data Pipeline Development
-   Pandas Data Processing
-   Data Cleaning Techniques
-   Data Validation Techniques
-   File Handling in Python
-   Exception Handling
-   Modular Project Structure
-   Git & GitHub Version Control

Future Enhancements

-   Convert pipeline to PySpark
-   Add logging framework
-   Add SQL database integration
-   Build Airflow scheduling
-   Deploy on Cloud
-   Create dashboard using Power BI

Author

Sharath Gourishetty
