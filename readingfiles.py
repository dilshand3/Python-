files = open('reading.txt','r')#this open take two parameter first is file name and second is 'r' is for reading

print(files.readable())#this is for checking that the file is readable or not it will show answer in true and false

print(files.readline())#this statement will print the first line of that file 

print(files.readline())#this statement will print the seconde line of that file

print(files.readline())#this statement will print the third line of that file

print(files.readline())#this statement will print the fourth line of that file

files.close()#we also have to close the file at last line

#this is the programe of reading external file 