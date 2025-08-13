# Write a program to create three lists of numbers, their squares and cubes

def create_list():
    num_list = []
    n = int(input("Enter the number of items in the list: "))
    for i in range(n):
        num = int(input("Enter a number:"))
        num_list.append(num)
        
    return num_list
    
def square_list(num_list):
    sq_list = []
    for x in num_list:
        sq_list.append(x**2)
        
    return sq_list
    
    
def cube_list(num_list):
    cu_list = []
    for x in num_list:
        cu_list.append(x**3)
        
    return cu_list
    
l1 = create_list()
l2 = square_list(l1)
l3 = cube_list(l1)
print(l1)
print(l2)
print(l3)