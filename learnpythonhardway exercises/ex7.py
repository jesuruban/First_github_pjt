#functions

def cheese_price(no_of_cheese,price_of_cheese):
	print("Let's print the total amount of the cheese\n")
	print("*"*25)
	print(no_of_cheese*price_of_cheese)
	print("*"*25)
	
#returns the value
def cheese_price_return(no_of_cheese,price_of_cheese):
	print("calculate and return the\
	value to main function\n")
	return no_of_cheese*price_of_cheese
	
#calling function with values
cheese_price(10,5)
#with variables
cheese_count=12
price=5
cheese_price(cheese_count,price)

#calling after doing calulation on the fly)
cheese_price(cheese_count+7,price)

#get input from user and call
cheese_count=int(input("enter cheese count... \n"))
price=int(input("cheese price... \n"))
cheese_price(cheese_count,price)

cheeseprice=cheese_price_return(cheese_count,price)
print("the prie from main function is %d" %cheeseprice)