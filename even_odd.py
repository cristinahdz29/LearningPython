
def even_odd():
    number = input("Tell me a number")
    even = int(number) % 2

    if even == 0:
        print('Your number is even')
    else:
        print('Your number is odd')

even_odd()