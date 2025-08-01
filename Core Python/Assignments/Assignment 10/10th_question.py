'''
Write a program to remove all occurrences of a given element in the list.
'''

def removeOccurrences(list1,target):
    new_list = []
    i = 0
    while i < len(list1):
        if (list1[i] != target):
            new_list.append(list1[i])
        i += 1

    return new_list

list1 = [2,3,4,2,2,5,6,2]
target = 2
new_list = removeOccurrences(list1,target)
print(f"The list after removing all occurrences of {target} is {new_list}")


# Removing all occurrences from the original list and returning it

def removeOccurrences(list1,target):
    i = 0
    while i < len(list1):
        if(list1[i] == target):
            del list1[i]
        else:
            i += 1
            
    return list1

list1 = [2,3,4,2,2,5,6,2]
target = 2
removeOccurrences(list1,target)
print(f"The list after removing all occurrences of {target} is {list1}")