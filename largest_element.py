numbers = [-1, -3, -200, -4]
largestNumber = numbers[0]
smallestNumber = numbers[0]

for i in numbers:
    if i > largestNumber:
        largestNumber = i
    elif i < smallestNumber:
        smallestNumber = i

print(f"{largestNumber} is the largest number")
print(f"{smallestNumber} is the smallest number")

# print(i)
# print(a)

