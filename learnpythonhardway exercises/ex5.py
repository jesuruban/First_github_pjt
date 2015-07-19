#files

from sys import argv
script=argv

print (argv)

file1=input("filename pls... ")
#opening the file in read mode and printing
file1_txt=open(file1)
print (file1_txt.read())
file1_txt.close()

#opening the file in write mode,truncating and adding again
file1_txt=open(file1,"w+")
new_lin1=input("enter the word u wish to add")
file1_txt.write(new_lin1)
print (file1_txt.read())
file1_txt.truncate()
new_lin1=input("enter the word u wish to add")
file1_txt.write(new_lin1)
print (file1_txt.read())
file1_txt.close()

#opening the file in append mode and adding lines
file1_txt=open(file1,"a+")
content=file1_txt.read()
print (len(content))
new_lin1=input("enter the word u wish to add")
file1_txt.write(new_lin1)
content=file1_txt.read()
print (len(content))
file1_txt.close()