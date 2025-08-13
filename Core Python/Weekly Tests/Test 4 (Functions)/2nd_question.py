# Write a program to find factorial of numbers in a given range using recursion

def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)

def factInRange(start,end):
    for num in range(start,end+1):
        ans = fact(num)
        print(f"Factorial of {num} is {ans}")
        
factInRange(1,5)
    