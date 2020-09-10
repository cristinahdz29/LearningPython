
# using predefined function to reverse to string

def palindrome():
    s = input("Give me a word: ")
    if(s == s[:: -1]):
        print("is a palindrome")
    else:
        print("is not a palindrome")

palindrome()


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
