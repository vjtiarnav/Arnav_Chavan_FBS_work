# Python Program to Check if a Given Key Exists in a Dictionary or Not

# Approach 1

def is_key_present(k):
    
    dict1 = {'a':'Mumbai','b':'Dubai','c':'Bahrain','d':'Doha'}
    
    for key in dict1:
        if key == k:
            return key, dict1[key]
    else:
        return -1,-1

k = input("Enter a key: ")
key1, value1 = is_key_present(k)

if (key1 != -1 and value1 != -1):
    print(f"{key1} is present in the dictionary and it's value is {value1}")
else:
    print(f"{k} is not present in the dictionary")
    

# Approach 2

def is_key_present(k):
    dict1 = {'a': 'Mumbai', 'b': 'Dubai', 'c': 'Bahrain', 'd': 'Doha'}
    return (k, dict1[k]) if k in dict1 else (-1, -1)

k = input("Enter a key you want to find: ")
key1, value1 = is_key_present(k)

if (key1 != -1 and value1 != -1):
    print(f"{key1} is present in the dictionary and it's value is {value1}")
else:
    print(f"{k} is not present in the dictionary")