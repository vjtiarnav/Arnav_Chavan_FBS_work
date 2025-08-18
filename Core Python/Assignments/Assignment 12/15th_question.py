# Python Program to find lexicographically larger string without using built-in functions.

def get_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def larger_string(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()

    len1 = get_length(str1)
    len2 = get_length(str2)
    
    if len1 > len2:
        return str1
    elif len2 > len1:
        return str2
    else:
        # If lengths are equal, compare character by character
        for i in range(len1):
            if str1[i] > str2[i]:
                return str1
            elif str2[i] > str1[i]:
                return str2
        return "Both strings are equal"

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = larger_string(str1, str2)
print("Larger string is:", result)