def initial():
    answer= input('''What would you like to do
            1. adding
            2.subtract
            3.divide
            4.division
            5.remainder after a division
            6.multiply
            7.quit
            ''')
    if answer == "1":
        print("You can now add numbers together")
        adding()
    elif answer == "2":
        print("You can now subtract numbers from each other")
        subtract()
    elif answer == "3":
        print("You can now divide number together")
        divide()
    elif answer == "4" :
        print("You can now do division with 2 numbers")
        division()
    elif answer == "5":
        print("You can find the remainder after a division")
        reminder()
    elif answer == "6":
        print("You can now multiply numbers together")
        multiply()
    elif answer == "7":
        print("I believe you are making a terrible mistake by deciding to quit. But see you later.BYE")
    else:
        print("Please enter a relevant answer ")

def adding():
	#adding
	number1 = int(input("Please input a number"))
	number2 = int(input("please input another number"))
	total = number1 + number2
	print ("the total is" , total)

def subtract ():
	#subtract
	number1 = int(input("Please input a number"))
	number2 = int(input("please input another number"))
	total = number1 - number2
	print ("the total is" , total)
#multiply
def multiply():
	number1 = int(input("Please input a number"))
	number2 = int(input("please input another number"))
	total = number1 * number2
	print ("the total is" , total)
	
def divide ():
	#divide
	number1 = int(input("Please input a number"))
	number2 = int(input("please input another number"))
	total = number1 / number2
	print ("the total is" , total)
	
def division():
	#whole number division
	number1 = int(input("Please input a number"))
	number2 = int(input("please input another number"))
	total = number1 // number2
	print ("the total is" , total)
	
def reminder():
	#reminder after whole number division
	number1 = int(input("Please input a number"))
	number2 = int(input("please input another number"))
	total = number1 % number2
	print ("the total is" , total)
initial()

