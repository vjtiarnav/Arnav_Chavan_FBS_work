# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

def count_word_frequency(input_string):
    word = ""
    word_count = {}
    
    for char in input_string:
        if char != ' ':
            word += char
        else:
            if word != "":
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
                word = ""  # Reset word for the next one
    
    # Add the last word if string doesn't end with a space
    if word != "":
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

user_input = input("Enter a string: ")
result = count_word_frequency(user_input)

# Print word frequencies
print("Word Frequencies:")
for word in result:
    print(f"'{word}': {result[word]}")