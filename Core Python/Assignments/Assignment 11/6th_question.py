# Python Program to Find the Union of Two Lists

def unionOfList(list1, list2):

    new_list = []
    for item in list1 + list2: # Duplicates are not allowed in union of two lists
        if item not in new_list: 
            new_list.append(item)

    return new_list

list1 = [1,2,3,4]
list2 = [4,5,6,7,8]
unionList = unionOfList(list1,list2)
print(f"Union of {list1} and {list2} is {unionList}")