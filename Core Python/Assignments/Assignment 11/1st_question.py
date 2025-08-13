# Python Program to Put Even and Odd elements of a List into two Different Lists
def separateEvenOdd(list1):
    e_list = []
    o_list = []
    
    for num in list1:
        if num % 2 == 0:
            e_list.append(num)
        else:
            o_list.append(num)
            
    return e_list, o_list
    
list1 = [1,2,3,4,5,6,7,8,9,10]
even_list, odd_list = separateEvenOdd(list1)
print(f"List with even numbers is {even_list} and list with odd numbers is {odd_list}")