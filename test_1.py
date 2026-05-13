import pandas as pd

d={'categories':['A','B','C','A'],'Values1':[20,30,40,50],'Values2':[50,60,70,60],
   'items':['aa','bb','cc','dd']}
df=pd.DataFrame(d)
#print(df)
#print(df['Values1'].sum())

#group1=df.groupby('categories')

#df=group1['Values1'].sum()
#print(df)

#df1=df.groupby('categories').agg({'Values1':'sum','Values2':'count'})

df2=df.groupby(['categories','items']).agg({'Values1':'sum','Values2':'count'})
print(df2)