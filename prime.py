

# prime number is always greater than 1

def prime_function():
    # set a variable equal to true, so it assumes that it is prime
    is_prime = True
    # Obtaining input from the user, and converting it to an integer so we can use it in the function
    number = int(input("Enter any number: "))

    if number < 1:
        return("This number is neither composite nor prime")
    else:
        for i in range(2, number):
            if (number % i) == 0:
                is_prime = False
                break

    if is_prime == True:
        return("The number is prime")
    else:
        return("Not a prime number")
        

print(prime_function())