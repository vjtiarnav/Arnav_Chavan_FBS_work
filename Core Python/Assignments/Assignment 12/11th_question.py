# Python Program to replace every blank space with hyphen in a string.

def replace_space_with_hyphen(input_string):
    result = ""
    for char in input_string:
        if char == ' ':
            result += '-'
        else:
            result += char
    return result

user_input = "This is a sample string"
output = replace_space_with_hyphen(user_input)
print("Modified string:", output)