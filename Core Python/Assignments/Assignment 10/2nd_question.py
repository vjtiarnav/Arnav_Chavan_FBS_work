'''
Write a program to find maximum and minimum element in a list.
'''

def minElement(list1):
    minimum = list1[0]
    min_index = 0
    for i in range(1,len(list1)):
        if (minimum > list1[i]):
            minimum = list1[i]
            min_index = i
    return minimum,min_index
            
def maxElement(list1):
    maximum = list1[0]
    max_index = 0
    for i in range(1,len(list1)):
        if(maximum < list1[i]):
            maximum = list1[i]
            max_index = i
    return maximum, max_index
        
list1 = [2,4,6,10,3,1]
minimum,minPos = minElement(list1)
maximum,maxPos = maxElement(list1)

print(f"The minimum element is the list {list1} is {minimum} and is found at index {minPos}")
print(f"The maximum element is the list {list1} is {maximum} and is found at index {maxPos}")