#print

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'


print ("hai how are you %s" %my_hair)
print ('hai \\ \n')
print (r'hai \\ \n')

#convert inches into centimeters
cal_variable=2.54

inp_inch=5
inp_centi=inp_inch*cal_variable
print (" %d inches equals to %r centimeters" %(inp_inch,inp_centi))

#more printing
print ("."*25)
print ("-"*25)

end1="tm"
end2="vsdv"
end3="sd"

print (end1+end2)
print (end3)

#more printing
day="mon"
days = "Mon \" \'Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print ("Here are the days: %r" %days)
print ("days %s" %days)
print ("Here are the \"months: ", months)

print ("""
There's something going on here.
With the three double- quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")


#for fun

#fun 
#while True:
#	for i in ["/","- ","|","\\","|"]:
#		print ("%s\r" % i)