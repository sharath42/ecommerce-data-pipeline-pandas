
#d={}
#print(type(d))

d={1:23,2:45,'abc':'sharath'}
#print(d.get(1))
#print(d.keys())
#print(d.values())
#print(d.items())
#d.update({'g':45})
#print(d)

#for i in d.values(): #to know for values in dictionary
    #print(i)
#for i in  d.keys(): #to know for keys in dictionary
    #print(i)

for i,j in  d.items(): #to know both  keys  and values in dictionary
    print(i,j)