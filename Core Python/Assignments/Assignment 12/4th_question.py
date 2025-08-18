# Python Program to Form a New String where the First Character and the Last Character have been Exchanged

# Approach 1

def exchange_character(str1):
    result = ''
    n = len(str1)
    for i in range(n):
        if i == 0:
            result += str1[n-1]
        elif i == n - 1:
            result += str1[0]
        else:
            result += str1[i]

    return result

str1 = input("Enter a string: ")
ans = exchange_character(str1)
print(f"The new string after exchanging the first and last character is {ans}")

# Approach 2

def exchange_character(s):
    n = len(s)
    if n <= 1:
        return s 

    return s[-1] + s[1:-1] + s[0]

str1 = input("Enter a string: ")
ans = exchange_character(str1)
print(f"The new string after exchanging the first and last character is: {ans}")