#functions with files

def rewind(f):
	f.seek(0)

def read(f):
	print (f.read())
	
def read_line(line_nbr,f):
	print ("Reading line %d:" %line_nbr,f.readline())

#open the file
inp_file="ex8.txt"
current_file=open(inp_file)

print ("Read the file")
read(current_file)

print ("Rewind the file\n")
rewind(current_file)

print ("Read line by line")
read_line(1,current_file)
read_line(2,current_file)