'''
Write a program to create a new list from existing list which contains cube of
each number of list.
'''

def Cube(list1):
    cube_list = []
    for num in list1:
        cube_list.append(num**3)
    
    return cube_list
    
list1 = [2,3,8,9,7]
cube_list = Cube(list1)
print(f"The new list containing cube of numbers from original list is {cube_list}")