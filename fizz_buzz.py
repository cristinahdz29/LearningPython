# Instructions: CREATE AN APP THAT TAKES IN INPUT FROM THE USER, IF ITS DIVISBLE BBY 3, PRINT FIZZ, IF ITS DIVISIBLE BY 5 PRINT BUZZ AND IF ITS DIVISIBLE BY BOTH, PRINT FIZZBUZZ
# STEP 1: GET INPUT FROM THE USER, AND PUT THE "INT" FUNCTION IN FRONT TO MAKE IT AN INTEGER, BECAUSE IT NEEDS TO BE AN INTEGER TO PERFORM MATH OPERATIONS


# Redone
# ask user for input
# number = int(input("Give me a number: "))

# if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
# elif number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print("Sorry! Your number is not divisible by 3 or 5")


#Putting it into a function
# Here I set an empty variable called answer, which is where i will store the answer to each case
# then i will return the answer at the end
# and when i print the function, I will get the answer I want

def fizzbuzz():
    answer = ""
    number = int(input("Give me a number: "))
    if number % 3 == 0 and number % 5 == 0:
        answer = "FizzBuzz"
    elif number % 3 == 0:
        answer = 'Fizz'
    elif number % 5 == 0:
        answer = "Buzz"
    else:
        print("Sorry! Your number is not divisible by 3 or 5")
    return answer

print(fizzbuzz())