'''
Write a program to remove duplicates from the list.
'''

def removeDuplicates(list1):
    new_list = []
    for num in list1:
        if num not in new_list:
            new_list.append(num)

    return new_list

list1 = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = removeDuplicates(list1)
print(f"The list after removing duplicates is {unique_list}")