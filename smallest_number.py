numbers = [200, 1, 3, 4]
smallestNumber = numbers[0]

for i in numbers:
    if i < smallestNumber:
        smallestNumber = i

print(f"{smallestNumber} this is the smallest number")
