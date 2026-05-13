#Filtering and sorting in Dataframe
import pandas as pd

#d1={'Name':['sharath','Mehul','Yaswanth','Lokesh'],'Age':[20,30,30,35]}
#t1=pd.DataFrame(d1)
#c=t1[(t1['Age']>=30)] # Single condition filter
#s=c.sort_values(by='Age',ascending=False) 
#Sorting data into descending order by change ascending =False
#print(s)


###d2={'Name':['s1harath','Mehul','Yaswanth','Lokesh'],'Age':[20,30,35,45]}
#t2=pd.DataFrame(d2)
#c1=t2[(t2['Age']>=30) & (t2['Name']!='Mehul')] #Multiple conditions infiltering the data
#s1=c1.sort_values(by='Age',ascending=False) #Default it taking the ascending order in sorting
#test1=s1.sort_index()
#print(test1)

d3={'Name':['Sharath','Yaswanth','Mehul'],'Age':[26,26,26],'salary':[20000,30000,2000]}
t3=pd.DataFrame(d3)
c3=t3[(t3['Age']>=26) & (t3['Name'] !='Mehul') & (t3['salary'] >=20000)]
d3=c3.sort_values(by='Age', ascending=False)
print(d3)


