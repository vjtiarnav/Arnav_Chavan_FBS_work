'''
Write a program to reverse the list.
'''

def reverseList(list1):
    print(list1[::-1])

list1 = [10,45,36,27,70]
print(f"The reversed list is: ")
reverseList(list1)


# Another Approach

def reverseList(list1):
    return list1[::-1]

list1 = [10, 45, 36, 27, 70]
reversed_list = reverseList(list1)
print(f"The reversed list is: {reversed_list}")