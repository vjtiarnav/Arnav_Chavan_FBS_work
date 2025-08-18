# Python Program to Take in a String and Replace Every Blank Space with Hyphen

# Approach 1

def replace_blank(str1):
    result = ''
    for ch in str1:
        if ch == " ":
            result += '-'
        else:
            result += ch
    return result

str1 = input("Enter a string: ")
ans = replace_blank(str1)
print(f"The string after replacing blank spaces with hypen is {ans}")

# Approach 2

str1 = input("Enter a string: ")
ans = str1.replace(' ', '-')
print(f"The string after replacing blank spaces with hyphen is: {ans}")