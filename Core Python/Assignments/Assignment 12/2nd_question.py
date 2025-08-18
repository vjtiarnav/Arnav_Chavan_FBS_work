# Python Program to Remove the nth Index Character from a Non-Empty String

def remove_nth_char(str1,n):
    if n < 0 or n >= len(str1):
        return "Index out of range."
    
    return str1[:n] + str1[n+1:]
    
str1 = input("Enter a string: ")
n = int(input("Enter the index whose character has to be removed: "))
ans = remove_nth_char(str1,n)
print(f"The string after removing {n}th index character from {str1} is '{ans}' ")