

#  ADDITION FUNCTION

def addition(number1, number2):
    return int(number1) + int(number2)


# total_1 = addition(number1, number2)

# print(total_1)

# SUBTRACTION FUNCTION

def subtraction(number1, number2):
    return int(number1) - int(number2)


# total_2 = subtraction(number1, number2)

# print(total_2)


# MULTIPLICATION

def multiply(number1, number2):
    return int(number1) * int(number2)


# total_3 = multiply(number1, number2)

# print(total_3)

def divide(number1, number2):
    return int(number1) / int(number2)


# total_4 = divide(number1, number2)

# print(total_4)

number1 = input("What is your first number? ")
number2 = input("What is your second number? ")
operand = input("What operation do you want?")
if operand == "+":
    result = addition(number1, number2)
    print(result)
elif operand == "-":
    result2 = subtraction(number1, number2)
    print(result2)
elif operand == "*":
    result3 = multiply(number1, number2)
    print(result3)
elif operand == "/":
    result4: divide(number1, number2)
    print(result4)

