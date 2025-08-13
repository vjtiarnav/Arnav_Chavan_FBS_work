# Python Program to Find the Intersection of Two Lists

def intersectionOfLists(list1, list2):
    new_list = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j] and list1[i] not in new_list:
                new_list.append(list1[i])

    return new_list

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
intersectionList = intersectionOfLists(list1, list2)
print(f"Intersection of {list1} and {list2} is {intersectionList}")