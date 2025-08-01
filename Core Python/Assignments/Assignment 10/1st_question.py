'''
Write a program to find sum of all elements of list
'''

list1 = [10,15,16,20,36,40]
listSum = 0

for num in list1:
    listSum += num

print(f"The sum of all elements in the list {list1} is {listSum}")


# Using functions

def SumofList(list1):
    total = 0
    for num in list1:
        total += num
    
    return total
    
list1 = [10,20,30,40,50]
ans = SumofList(list1)
print(f"The sum of all elements in the list {list1} is {ans}")