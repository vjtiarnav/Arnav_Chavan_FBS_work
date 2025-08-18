# Python Program to count the occurrences of each word in a string.

def count_word_occurrences(input_string):
    words = []
    word = ""

    # Manually split the input into words (on spaces)
    for char in input_string:
        if char != ' ':
            word += char
        else:
            if word != "":
                words.append(word)
                word = ""
    
    # Add the last word if it exists
    if word != "":
        words.append(word)

    # Count word occurrences using a dictionary
    word_count = {}
    for w in words:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1

    return word_count

user_input = "this is a test this is only a test"
result = count_word_occurrences(user_input)
for word in result:
    print(f"'{word}': {result[word]}")