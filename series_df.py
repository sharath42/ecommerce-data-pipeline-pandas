#introduct1ion to pandas for series and dataframe creation
import pandas as pd
import numpy as np

#d1=[1,2,3,4,5] #covert list into series
#series=pd.Series(d1)
#print(series)

#d2=[6,7,8,9,10] #renaming the indexes of the list
#index=['a','b','c','d','e']
#series1=pd.Series(d2,index=index) #method 1
#series1=pd.Series(d2,index=['a','b','c','d','e']) #method 2
#print(series1)

#d3={'a':1,'b':2,'c':3,'d':4} #covert dictionary into series
#t3=pd.Series(d3)
#print(t3)

#Examples for Dataframes 

#d4=[[1,'a'],[2,'b'],[3,'c']] #covert list into dataframe
#t4=pd.DataFrame(d4)
#print(t4)

#d5=[[1,'a'],[2,'b'],[3,'c']] #Giving names to the columns of the dataframe
#com=['id','Name']
#t5=pd.DataFrame(d5,columns=com)
#print(t5)

d6={'id':[1,2,3],'Name':['sharath','mehul','yaswanth']} #convert Dictionary into Dataframes
ind=[1,2,3]
t6=pd.DataFrame(d6,index=ind)
print(t6)