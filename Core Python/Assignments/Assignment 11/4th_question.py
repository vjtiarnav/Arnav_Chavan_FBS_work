# Python Program to Find the Second Largest Number in a List Using Bubble Sort

def bubbleSort(list1):
    n = len(list1)
    for i in range(n):
        for j in range(0, n-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    
    # Return the second largest number
    return list1[-2]

list1 = [30, 2, 45, 20, 15]
ans = bubbleSort(list1)
print("Second largest number:", ans)