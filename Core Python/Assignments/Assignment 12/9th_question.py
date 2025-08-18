# Python Program to Calculate the Number of Words and the Number of Characters Present in a String

def word_and_char_count(str1):

    word_count = 0
    char_count = 0
    in_word = False

    for ch in str1:
        
        char_count += 1

        if ch != " " and not in_word:
            word_count += 1
            in_word = True

        elif ch == " ":
            in_word = False
    
    return word_count, char_count

str1 = input("Enter a string: ")
w_count, c_count = word_and_char_count(str1)
print(f"The number of words in \"{str1}\" is {w_count} and the number of characters is {c_count}")