# needed to create a function that removes duplicates
# this is my list of names to test
# this is where we used a dictionary, because if have 2 keys and values equal to each other, they won't repeat
# then we use dict.keys() to just get all the keys, which are the names
# then use we list, to turn it back into a list, so we can print it out
names = ["alex", "John", "Mary", "Steve", "John", "Steve", "Ana", "Ana"]
dict = {}

def duplicates():
    for name in names:
        dict[name] = True
    # print(dict)
        

    return(list(dict.keys()))


print(duplicates())
    
