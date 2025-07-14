# WAP to print all odd numbers until n.

n = int(input("Enter a number: "))
count = 0
for i in range(1,n+1):
    if(i%2!=0):
        print(i)
        count += 1
        
print(f"The number of odd numbers from 1 to {n} are {count}")