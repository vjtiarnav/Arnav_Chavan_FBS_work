'''
Accept a number from user and check if this element is present in the list or
not. Also tell how many times it is present in the list.
'''
def isPresent(list1,target):
    count_of_target = 0
    for i in range(len(list1)):
        if list1[i] == target:
            count_of_target += 1
    
    return count_of_target
    
list1 = [1, 2, 5, 7, 7, 10, 8, 7, 7]
target = int(input("Enter a number you want to find: "))

ans = isPresent(list1,target)

if(ans == 0):
    print(f"{target} is not present in the list")
else:
    print(f"{target} is present in the list and it occurs {ans} time(s)")



# Improvization of the above method by returning the indices at which target is present

def isPresent(list1, target):
    count_of_target = 0
    indices = []
    for i in range(len(list1)):
        if list1[i] == target:
            count_of_target += 1
            indices.append(i)
    
    return count_of_target, indices
    
list1 = [1, 2, 5, 7, 7, 10, 8, 7, 7]
target = int(input("Enter a number you want to find: "))

count, indices = isPresent(list1, target)

if count == 0:
    print(f"{target} is not present in the list")
else:
    print(f"{target} is present in the list and it occurs {count} time(s) at indices {indices}")