# print(total_4)
# instructions:
# build a calculator that takes in 3 inputs from the user:
# input 1 = first number
# input 2 = operand (-, +, *, /)
# input 3 = second number
# based on the operand that is input, we will preform that operation with the 2 numbers and return the result
# each operation must be a seperate function

# Step 1: create functions for each math operation, so we can call them later when we put it all together


#  CREATING ADDITION FUNCTION
# TO CREATE AN ADDITION FUNCTION, THE 2 PARAMETERS NEEEDED ARE THE NUMBERS, YOU DONT NEED THE OPERAND AT THIS POINT BECAUSE YOURE ALREADY ADDING IN THE FUNCTION, SO IF THEY PROVIDE THE + OPERAND, THEN THIS FUNCTION WILL RUN
# THIS FUNCTION WILL RETURN THE SUM OF THE 2 NUMBERS THE USER INPUT, WHICH IS WHAT WE WANT TO DO IF THEY PROVIDE THE + OPERAND

def addition(number1, number2):
    return int(number1) + int(number2)


# CREATING SUBTRACTION FUNCTION
# TO CREATE A SUBTRACTION FUNCTION, THE 2 PARAMETERS NEEEDED ARE THE NUMBERS, YOU DONT NEED THE OPERAND AT THIS POINT BECAUSE YOURE ALREADY SUBTRACTING IN THE FUNCTION, SO IF THEY PROVIDE THE + OPERAND, THEN THIS FUNCTION WILL RUN
# THIS FUNCTION WILL RETURN THE DIFFERENCE OF THE 2 NUMBERS THE USER INPUT, WHICH IS WHAT WE WANT TO DO IF THEY PROVIDE THE - OPERAND

def subtraction(number1, number2):
    return int(number1) - int(number2)


# CREATING MULTIPLICATION FUNCTION
# TO CREATE A MULTIPLICATION FUNCTION, THE 2 PARAMETERS NEEEDED ARE THE NUMBERS, YOU DONT NEED THE OPERAND AT THIS POINT BECAUSE YOURE ALREADY MULTIPLYING IN THE FUNCTION, SO IF THEY PROVIDE THE * OPERAND, THEN THIS FUNCTION WILL RUN
# THIS FUNCTION WILL RETURN THE PRODUCT OF THE 2 NUMBERS THE USER INPUT, WHICH IS WHAT WE WANT TO DO IF THEY PROVIDE THE * OPERAND

def multiply(number1, number2):
    return int(number1) * int(number2)

# CREATING DIVISION FUNCTION
# TO CREATE A DIVISION FUNCTION, THE 2 PARAMETERS NEEEDED ARE THE NUMBERS, YOU DONT NEED THE OPERAND AT THIS POINT BECAUSE YOURE ALREADY DIVIDING IN THE FUNCTION, SO IF THEY PROVIDE THE / OPERAND, THEN THIS FUNCTION WILL RUN
# THIS FUNCTION WILL RETURN THE DIVISION OF THE 2 NUMBERS THE USER INPUT, WHICH IS WHAT WE WANT TO DO IF THEY PROVIDE THE * OPERAND


def divide(number1, number2):
    return int(number1) / int(number2)


# THIS IS WHERE WE ASK THE USER FOR THE INPUTS, WHICH IS THE 2 NUMBERS THEY WANT TO PREFORM A CALCULATION WITH, AND THE SYMBOL OF THE MATH OPERATION THEY WANT TO PREFORM AND SAVING THEM TO VARIABLES SO WE CAN ACCESS THEM LATER
# print("Hi! I'm your personal calculator! Lets do some calculating!!")
# number1 = input("What is your first number? ")
# operand = input("What operation do you want? ")
# number2 = input("What is your second number? ")
# if operand != '+' and operand != '-' and operand != '*' and operand != '/':
#     print("This is not a valid operand. Please enter one of the following: +, -, *, /")

    


# HERE WE ARE MAKING IF STATEMENTS THAT WILL RUN DEPENDING ON WHAT OPERAND THE USER ENTERED
# IF THE OPERAND THE USER ENTERED IS +, THEN WE WILL CALL THE ADDITION FUNCTION, AND BRING IN THE 2 NUMBERS THEY INPUT, WHICH ARE NOW LIVING IN THE NUMBER1 AND NUMBER2 VARIABLES
# WE SET THE RESULT OF THE FUNCTION TO A VARIABLE CALLED RESULT, AND THEN WE PRINTED THAT
# WE DO THIS FOR EACH POSSIBLE OPERAND THAT CAN BE ENTERED
# I MADE IT INTO A FUNCTION
def calculator():
    print("Hi! I'm your personal calculator! Lets do some calculating!!")
    number1 = input("What is your first number? ")
    operand = input("What operation do you want? ")
    number2 = input("What is your second number? ")
    if operand == "+":
        result = addition(number1, number2)
        print(f"The answer is {result}")
    elif operand == "-":
        result = subtraction(number1, number2)
        print(f"The answer is {result}")
    elif operand == "*":
        result = multiply(number1, number2)
        print(f"The answer is {result}")
    elif operand == "/":
        result: divide(number1, number2)
        print(f"The answer is {result}")
    else:
        print("This is not a valid operand. Please enter one of the following: +, -, *, /")

calculator()