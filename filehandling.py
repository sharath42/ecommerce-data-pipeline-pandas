#with open(r"C:/Users/91728/OneDrive/Desktop/mehul.txt") as mehul:
#s=open("C:/Users/91728/OneDrive/Desktop/test.txt",mode='a')
#s.append("Sharath is a good boy")
#s.seek(0)
#print(s.read())
#s.close()



#test_file=open("sharath.txt",mode='w') #write in file
#test_file.write("Tcs erripukudhi")
#print(test_file.read())
#test_file.close()

#test_file1=open("sharath.txt",mode='r+') #R+ indicates read and write in file at same time
#print(test_file1.read())
#test_file1.seek(0)
#test_file1.write("Thagubothu Yashwanth")
#test_file1.close()

test_file1=open("sharath.txt",mode='a') #a indicates append data at end of the file 
test_file1.append("Vad pedda pichi pukugadu")
test_file1.close()