# Write a program to print list after removing even numbers.

def remove_even(list1):
    i = 0
    while i < len(list1):
        if list1[i] % 2 == 0:
            del list1[i]
        else:
            i += 1
            
    return list1
    
l1 = [1,2,3,4,5,6,7,8]
odd_numbers = remove_even(l1)
print(odd_numbers)