
# using predefined function to reverse to string

# def palindrome():
#     string = input("Give me a word: ")
#     if(string == string[:: -1]):
#         print("is a palindrome")
#     else:
#         print("is not a palindrome")

# palindrome()

def palindrome():
    string = input("Give me a word: ")
    new_string = []
    for i in range(len(string)-1, -1, -1):
        new_string.append(string[i])
    updated_string = ''.join(new_string)
    if string == updated_string:
        return "This is a palindrome"
    else:
        return "This is not a palindrome"
    

print(palindrome())


# check if both strings are equal
#     if rev == s:
#         return True
#     return False
# if True:
#     print("Is a palindrome")
# else:
#     print("You suck")


# Main function
# s= "mom"
# answer = palindrome(s)
# if (answer):
#     print("True")
# else:
#     print("no")

    # palindrome_check = []
    # word = input("Give me a word: ")

    # for character in word[::-1]:
    #     palindrome_check.append(character)

    #     new_string = " ".join(palindrome_check)

    #     print(new_string)

    # if new_string == word:
    #     print("This is a palindrome")
    # else:
    #     print("This is not a palindrome")

    # is_palindrome = True
    # word = input('Give me a word: ')

    # for i in range(0, len(word)):
    #     if str(i) != str[len(str)-i-1];
    #     return False
    # return True
