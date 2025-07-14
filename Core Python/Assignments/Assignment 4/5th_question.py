# WAP to print Fibonacci series upto n.

n = int(input("Enter the number of terms you want in Fibonacci series: "))
a = -1
b = 1

for i in range(n):
    c = a + b
    print(c)
    a = b
    b = c