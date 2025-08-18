# Python Program to Remove the Given Key from a Dictionary

def removeKey(my_dict, k):
    if k in my_dict:
        del my_dict[k]
    return my_dict

my_dict = {'a': 10, 'b': 20, 'c': 30}
k = input("Enter the key you want to remove: ")
dict1 = removeKey(my_dict, k)
print(dict1)