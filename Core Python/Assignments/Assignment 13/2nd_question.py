# Python Program to Concatenate Two Dictionaries Into One

def concatenate_dicts(dict1, dict2):
    merged = {}

    for key in dict1:
        merged[key] = dict1[key]
    
    for key in dict2:
        merged[key] = dict2[key]
    
    return merged

dict1 = {'x': 100, 'y': 200}
dict2 = {'z': 999, 'w': 300}  # Note: 'y' key will be overwritten

merged_dict = concatenate_dicts(dict1, dict2)
print("Merged Dictionary:", merged_dict)