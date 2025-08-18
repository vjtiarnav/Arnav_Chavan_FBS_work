# Python Program to Sum All the Items in a Dictionary

# Approach 1

def sum_dictionary_values(my_dict):
    total = 0
    for key in my_dict:
        value = my_dict[key]
        total += value
    return total

sample_dict = {'a': 10, 'b': 20, 'c': 30}
result = sum_dictionary_values(sample_dict)
print("Sum of all values in the dictionary:", result)

# Approach 2

sample_dict = {'a': 10, 'b': 20, 'c': 30}

total = sum(sample_dict.values())
print("Sum of all values in the dictionary:", total)

