# Write an app which asks users for the input and then prints the factorial for that number. 
# A FACTORIAL NUMBER IS ONE THAT IS MULTIPLIED BY ALL THE NUMBERS BEFORE IT, LIKE 6, WILL BE 6*5*4*3*2*1
# STEP 1: MAKE A FUNCTION
# STEP2: WE NEED TO GET INPUT FROM THE USER, AND MAKE IT AN INTEGER SO WE CAN DO MATH OPERATIONS WITH IT
# STEP 3: WE WILL NEED A FOR LOOP? BECAUSE WE NEED TO BE ABLE TO ACCESS THE NUMBERS FROM 1 TO THE USER INPUT
# TAKING INDEX
# the second argument for range is not inclusive, so it will only go up to 4
# So what we're doing is looping through the numbers 1 -4, and setting the variable number = to the input, so we start with that number, and we loop and multiply it by every number up until 4, it doesn't need to be inclusive because we already accounted for multiplying by 5 in the beginnning when we set the number variable equal to 5, and we multiplied it up until 5.
# we kept making the number variable equal to number times i so that the product keep compounding
# 5 * 1*2*3*4 is the same thing as 5*4*3*2*1, which is why the loop works

def factorial_problem():
    number = int(input("Tell me a number:"))
    for i in range(1, number):
        number = number * i
        print(i)
    print(number)



factorial_problem()