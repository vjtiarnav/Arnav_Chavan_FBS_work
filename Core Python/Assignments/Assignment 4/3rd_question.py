# WAP to print sum of series upto n.

n = int(input("Enter a number: "))
sumOfNumbers = 0

for i in range(1,n+1):
    sumOfNumbers += i

print(f"The sum of numbers from 1 to {n} is {sumOfNumbers}")