'''
Write a program to print all numbers which are divisible by m and n in the list.
'''
def commonDivisbleNumbers(list1,m,n):
    for num in list1:
        if(num % m == 0 and num % n == 0):
            print(num)
        
list1 = [1,2,6,12,15,18,21,24,27,30,33,36]
m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))
commonDivisbleNumbers(list1,m,n)