import pandas as pd
import numpy as np

d={'age':[1,2,np.nan,4],'id':[np.nan,6,np.nan,8]} #nan is a numpy function for missing numerical values
t=pd.DataFrame(d) 
s=t.isna() # isna is function to find where missing value is there
print(s)

d1={'age':[1,2,np.nan,4],'id':[np.nan,6,np.nan,8]} #nan is a numpy function for missing numerical values
t1=pd.DataFrame(d1) 
s1=t1.fillna(10) # fillna  is function to replace null value with specific value
print(s1)
