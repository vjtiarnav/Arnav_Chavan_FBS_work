# Python Program to Merge Two Lists and Sort it

def mergeAndSort(list1,list2):
    i = 0
    j = 0
    list3 = []
    while(i < len(list1) and j < len(list2)):
        if(list1[i] < list2[j]):
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1
            
    while i < len(list1):
        list3.append(list1[i])
        i += 1
        
    while j < len(list2):
        list3.append(list2[j])
        j += 1
        
    return list3
    
list1 = [3,8,10,15]
list2 = [5,6,23,45]
new_list = mergeAndSort(list1,list2)
print(f"The new list after merging and sorting the two given lists {list1} and {list2} is {new_list}")