import pandas as pd
import datetime as date;




d={'A':[1,2,3,4],'B':['5','6','7','8']}
t=pd.DataFrame(d)
t['B']=t['B'].astype(int) # astype() funtion is used to cast the dtype of columns
print(t.info()) #info() function is used to know the dtype of DataFrame