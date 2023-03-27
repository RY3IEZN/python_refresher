print("time to refresh my pyhon")

# data types
print("this is a string")
print(3)  #int
print(3.0)  #flaot
print(str(4))  #str
print(f"dddd {23} ddd")  #the f can detect a non string

# math ope
print(6 * 7, "dayd to go")

#vars
the_operation = 20 + 3 + 4
unit = "seconds"


# function
def calcuate_time(number_of_days, custom_message):
    print(f"{number_of_days} + {the_operation} {unit} {custom_message}")


calcuate_time(21, "great")
calcuate_time(31, "awseome")

# a function to get the user input
input("how many days: \n")

# set the users input int a value
user_input = input("how many days: \n")
print(user_input)

calcuate_time(user_input, "passing value")
