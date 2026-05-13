#Introduction to slicing and Indexing in Data frame
import pandas as pd

d1={'Name':['sharath','Mehul','Yaswanth','Karri Lokesh'],'Age':[20,25,30,35],
    'salary':[20000,30000,40000,50000]}
ind=['a','b','c','d']
df=pd.DataFrame(d1,index=ind) #Remaining the Indexes and converting Dictionary into Dataframe
#nam=df['Name'] #Indexing in Dataframe
#print(nam)
#print(df[0:3]) #Slicing in Dataframe
print(df.iloc[0:3]) #iloc function using to print rows by using indexing
print(df.loc['a']) #loc function used to show a specific row into a tabluar form