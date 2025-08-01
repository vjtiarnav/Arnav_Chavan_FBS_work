'''
Write a program to create three lists of numbers, their squares and cubes
'''
def createList(n):
    num_list = []
    for i in range(n):
        num = int(input("Enter a number: "))
        num_list.append(num)

    return num_list

def squareList(list1):
    square_list = []
    for num in list1:
        square_list.append(num**2)

    return square_list

def cubeList(list1):
    cube_list = []
    for num in list1:
        cube_list.append(num**3)

    return cube_list

n = int(input("Enter number of elements in the list: "))
list1 = createList(n)
list2 = squareList(list1)
list3 = cubeList(list1)

print(f"\nNumber List: {list1}")
print(f"Number Square List: {list2}")
print(f"Number Cube List: {list3}")