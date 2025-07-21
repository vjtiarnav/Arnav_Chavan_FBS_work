# Write a program to print first n prime numbers

n = int(input("Enter a number: "))
print(f"The prime numbers from 1 to {n} are: ")

for i in range(2,n+1):
    for j in range(2,i):
        if(i % j == 0):
            break
    else:
        print(i)

