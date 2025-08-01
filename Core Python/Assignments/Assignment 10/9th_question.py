'''
Write a program of having n number of elements in the list and find out even
and odd elements in that list and then create two separate lists which will have
even elements and other will have odd elements.
'''

def separateEvenOdd(list1):
    e_list = []
    o_list = []
    for num in list1:
        if(num % 2 == 0):
            e_list.append(num)
        else:
            o_list.append(num)
    return e_list,o_list

list1 = []

n = int(input("Enter number of elements in the list: "))
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    list1.append(num)

even_list, odd_list = separateEvenOdd(list1)
print(f"The list with even elements is {even_list}")
print(f"The list with odd elements is {odd_list}")