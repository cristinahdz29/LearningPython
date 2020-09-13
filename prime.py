# Assignment 3: Take input from the user and find out if that number is prime or not.
# A prime number is one that is divisible only by itself and 1, zero and one are not prime numbers
# In other words, prime number is always greater than 1, so that can be one condition that needs to be met to move forward
# Step 1: create a function; does not need parameters because we will get input from the user within the function

def prime_function():
    # set a variable equal to true, so it starts by assuming that it is prime
    is_prime = True
    # Obtaining input from the user, and converting it to an integer so we can use it in the function
    number = int(input("Enter any number: "))

    if number < 1:
        return("This number is neither composite nor prime")
    else:
        for i in range(2, number):
        # You need a for loop because you need to run through each number below the user input number and check if it is divisible by it, if it is divisible by it evenly, then it is not prime
        # the range has to start with 2, because all numbers are divisible by 1, so the only thing you need to determine is if it is divisible by any number smaller than it; you dont need to check numbers above it becauase that will only give you a decimal
        # if the number is even divisble, then is_prime becomes false

            if (number % i) == 0:
                is_prime = False
                break
    # Here we step out of the for loop, and if is prime = true, meaning the
    if is_prime == True:
        return("The number is prime")
    else:
        return("Not a prime number")
        

print(prime_function())
