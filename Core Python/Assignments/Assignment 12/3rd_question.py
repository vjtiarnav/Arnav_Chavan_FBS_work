# Python Program to Detect if Two Strings are Anagrams

def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if is_anagram(str1, str2):
    print(f"{str1} and {str2} are anagrams of each other")
else:
    print(f"{str1} and {str2} are not anagrams of each other")