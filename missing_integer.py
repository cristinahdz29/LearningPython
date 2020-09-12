numbers = [0, 1, 2, 3, 5, 6, 7, 8, 9]
# missing = numbers[1] 

# for i in numbers:
#     if i + 1 == numbers:
#         print(missing)


for x in range(0, len(numbers) - 1):
    numb1 = numbers[x+1]
    numb2 = numbers[x]
    if numb1 - numb2 != 1:
        print(numbers[x] + 1)
