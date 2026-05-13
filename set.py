#s={}
#print(type(s)) 

s={42,36,'sharath',69,42} # doesn't allow duplicates
s.add('gourishetty') #adding in set
s.update({12,56,'vinoda',63}) # adding bulk data in set use update
s.pop() #removes random element from set
s.remove('gourishetty') #removes specific element from the set
print(s) 

