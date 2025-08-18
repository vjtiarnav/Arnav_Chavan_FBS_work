# Python Program to Count the Number of Vowels in a String

def count_vowels(str1):

    count = 0

    for ch in str1:
        if ch.lower() in "aeiou":
            count += 1

    return count

str1 = input("Enter a string: ")
vowel_count = count_vowels(str1)
print(f"The number of vowels in \"{str1}\" is {vowel_count}")