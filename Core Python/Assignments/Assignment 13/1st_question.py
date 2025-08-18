# Python Program to Add a Key-Value Pair to the Dictionary

def add_key_value(my_dict, key, value):
    my_dict[key] = value
    return my_dict

my_dict = {'a': 10, 'b': 20}
print("Original Dictionary:", my_dict)

key = input("Enter the key to add: ")
value = input("Enter the value to add: ")

if value.isdigit():
    value = int(value)

updated_dict = add_key_value(my_dict, key, value)

print("Updated Dictionary:", updated_dict)