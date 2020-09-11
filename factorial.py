

def factorial_problem():
    number = int(input("Tell me a number:"))
    for i in range(1, number):
        number = number * i
        print(i)
    print(number)



factorial_problem()
