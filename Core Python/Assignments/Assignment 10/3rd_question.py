'''
Write a program to find the second largest element in the list.
'''
def secondLargestElement(list1):
    secondmax = 0
    firstmax = list1[0]
    for i in range(1,len(list1)):
        if (firstmax < list1[i]):
            secondmax = firstmax
            firstmax = list1[i]

    return secondmax

list1 = [10,20,30,40,50]
ans = secondLargestElement(list1)
print(f"The second largest element in the list {list1} is {ans}")