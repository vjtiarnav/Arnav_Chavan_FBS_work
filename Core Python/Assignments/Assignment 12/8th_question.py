# Python Program to Remove the Characters of Odd Index Values in a String

# Approach 1

def remove_char_at_oddIndex(str1):
    result = ''
    for i in range(len(str1)):
        if i % 2 == 0:
            result += str1[i]

    return result

str1 = input("Enter a string: ")
ans = remove_char_at_oddIndex(str1)
print(f"The string after removing characters of odd index values of original string \"{str1}\" is {ans}")

# Approach 2

def remove_char_at_oddIndex(s):
    return s[::2]

s = input("Enter a string: ")
ans = remove_char_at_oddIndex(s)
print(f"The string after removing characters of odd index values of original string \"{s}\" is {ans}")
