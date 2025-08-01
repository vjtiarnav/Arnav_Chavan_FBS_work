'''
Write a program to create a duplicate of an existing list. 
It should not point to same list.
'''

def duplicateList(list1):
    duplicate_list = []
    for num in list1:
        duplicate_list.append(num)
    
    return duplicate_list

list1 = [1,2,3,4,5]
duplicate_list = duplicateList(list1)
print(f"The duplicate of {list1} is {duplicate_list}")

# Proof of Concept
# Use id() -----> id(list1) and id(duplicate_list) will be different
