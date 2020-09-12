numbers = [0, 1, 2, 3, 5, 6, 7, 8, 9]
# missing = numbers[1] 

# for i in numbers:
#     if i + 1 == numbers:
#         print(missing)

def missing_integer(arr):
    for x in range(0, len(arr) - 1):
        numb1 = arr[x+1]
        numb2 = arr[x]
        if numb1 - numb2 != 1:
            print(arr[x] + 1)
