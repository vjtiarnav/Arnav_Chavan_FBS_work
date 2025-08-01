'''
Write a program to print list after removing even numbers.
'''
#Creating a new list and storing odd numbers in it

def removeEvenNumbers(list1):
    odd_numbers_list = []
    for num in list1:
        if num % 2 != 0:
            odd_numbers_list.append(num)

    return odd_numbers_list

list1 = [1,2,3,4,5,6,7,8]
new_list = removeEvenNumbers(list1)
print(f"The list after removing even numbers is {new_list}")

# Modifying the original list by removing even numbers from original list

def removeEvenNumbers(list1):
    i = 0

    while i < len(list1):
        if list1[i] % 2 == 0:
            del list1[i]
        else:
            i += 1
        
    return list1

list1 = [1,2,3,4,5,6,7,8]
removeEvenNumbers(list1)
print(f"The original list after removing even numbers is {list1}")