# Python Program to count number of digits and letters in a string.

def count_of_digits_and_letters(str1):
    
    digit_count = 0
    letter_count = 0

    for ch in str1:
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            letter_count += 1
        elif '0' <= ch <= '9':
            digit_count += 1
    
    return digit_count, letter_count

str1 = input("Enter a string: ")
d_count, l_count = count_of_digits_and_letters(str1)
print(f"The number of digits in \"{str1}\" is {d_count} and the number of letters is {l_count}")