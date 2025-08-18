# Python Program to Replace all Occurrences of ‘a’ with $ in a String

# Approach 1

def remove_occurrence(str1):
    new_str = ''

    for ch in str1:
        if ch == 'a':
            new_str += '$'
        else:
            new_str += ch
        
    return new_str

str1 = input("Enter a string: ")
ans = remove_occurrence(str1)
print(f"The string after replacing all occurences of 'a' with '$' is {ans}")

# Approach 2

str1 = input("Enter a string: ")
new_str = str1.replace('a','$')
print(str1)
print(new_str)