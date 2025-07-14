# WAP to print all numbers in a range divisible by a given number.

n = int(input("Enter the range limit: "))
div = int(input("Enter the number to divide by: "))

for i in range(1, n + 1):
    if i % div == 0:
        print(i, end=' ')
