number = input("Give me a number: ")

fizz = int(number) % 3

buzz = int(number) % 5


if fizz == 0 and buzz != 0:
    print('Fizz')
elif fizz != 0 and buzz == 0:
    print('Buzz')
elif buzz == 0 and fizz == 0:
    print("FizzBuzz")
else:
    print('Your number is not divisible by 3 or 5')
