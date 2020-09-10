

# prime number is always greater than 1

def prime_function():
    is_prime = True
    number = int(input("Enter any number: "))

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                is_prime = False
                break
    if is_prime == True:
        print("The number is prime")
    else:
        print("Not a prime number")
        

prime_function()