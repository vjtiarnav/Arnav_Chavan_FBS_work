# Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions

def find_length(s):
    count = 0
    for ch in s:
        count += 1

    return count

def find_larger_string(str1,str2):
    len1 = find_length(str1)
    len2 = find_length(str2)

    if len1 > len2:
        return str1
    elif len1 < len2:
        return str2
    else:
        return "Both strings are of equal length"
    

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

ans = find_larger_string(str1,str2)
print(f"Result: {ans}")