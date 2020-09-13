# Create an app which detects if the input word is a palindrome or not.
# Palindromes are strings which when read from left to right are same as right to left.

# STEP 1: CREATE A FUNCTION
# WE WILL NEED TO GET INPUT FROM THE USER, THE INPUT FUNCTION ALREADY BRINGS THE INPUT INTO STRING
# CREATED AN EMPTY ARRAY


def palindrome():
    # WE WILL NEED TO GET INPUT FROM THE USER, THE INPUT FUNCTION ALREADY BRINGS THE INPUT INTO STRING
    string = input("Give me a word: ")
    # CREATED AN EMPTY ARRAY
    new_string = []
    # CREATED A LOOP
    # LENGTH GIVE US THE NUMBER OF CHARACTERS, SO IF THE INPUT WORD IS 'MOM', THEN LENGHT IS 3
    # RANGE GIVES US THE INDEX, THE LENGHT IS ALWAYS 1 GREATER THAN THE INDEX BECAUSE INDEX ALWAYS STARTS WITH 0, SO WE NEED TO SUBTRACT ONE FROM THE LENGHT TO GET THE RIGHT INDEX,
    # SO WE WANT TO ARRANGE THE LETTERS IN REVERSE
    # SO WE NEED A FOR LOOP TO LOOP THROUGH THE WORD AND GET THE LETTERS
    # TO GET THE LETTERS IN REVERSE, WE WANT THE RANGE TO START AT THE END OF THE STRING (WHICH IS THE LENGHT OF THE STRING -1 BECAUSE THAT THE MAX NUMBER OF INDEX), THEN WE WANT TO STOP AT THE LAST ITEM (-1)
    # AND WE WANT TO DECREASE BY ONE
    for i in range(len(string)-1, -1, -1):
        new_string.append((string[i]))
    updated_string = ''.join(new_string)
    if string == updated_string:
        return "This is a palindrome"
    else:
        return "This is not a palindrome"


print(palindrome())

# Do palindrome without reversing string


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
