#files - write
from sys import argv
from os.path import exists
to_file="ex6_op.txt"

file1=input("filename pls... ")
file1_txt=open(file1)
content=file1_txt.read()
print ("length of the file file1 is",len(content))

print ("does the output file exist%r" %exists(to_file))

#out_file=open(to_file,'w+')
#out_file.write(content)

#print (out_file.read())
 


