# Python Program to count number of lowercase characters in a string.

def count_lowercase_char(str1):
    count = 0
    for ch in str1:
        if 'a' <= ch <= 'z':
            count += 1
    return count

str1 = input("Enter a string: ")
lowercase_count = count_lowercase_char(str1)
print(f"The number of lower-case characters in \"{str1}\" is {lowercase_count}")