arr = [42, 10, 25, 20, 19]

def duplicate(arr):
    for i in range(0, len(arr)-1):
        arr.append(arr[i])
    return arr

print(duplicate(arr))

    
