# Python Program to Sort a List According to the Length of the Elements within the list.

def sort_by_length(list1):
    
    n = len(list1)
    for i in range(n):
        for j in range(0,n-i-1):
            if len(list1[j]) > len(list1[j+1]):
                list1[j],list1[j+1] = list1[j+1],list1[j]
                
    return list1
    
l1 = ["One","Seventeen",['A','B'],"Python","K"]
sorted_list = sort_by_length(l1)
print(sorted_list)