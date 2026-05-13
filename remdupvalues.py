import pandas as pd
import numpy as np

d={'A':[1,2,3,4,5,1],'B':[6,7,8,9,10,6]}
t=pd.DataFrame(d)
#s=t.duplicated().value_counts() #duplicated and values_count functions are used to know the count of duplicates in the data
t=t[t.duplicated().values] # this is used to know what are the duplicated values in the data
#t=t.drop_duplicates() #this function is used to remove duplicates from the data
print(t) 