# WAP to print Armstrong number within a given range

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

print(f"\nArmstrong numbers between {start} and {end} are: ")
for num in range(start, end+1):
    temp = num
    digits = 0
    sumOfDigits = 0

    while(temp>0):
        digits += 1
        temp = temp // 10
    
    temp = num
    while(temp>0):
        digit = temp % 10
        sumOfDigits += digit**digits
        temp = temp // 10
    
    if(sumOfDigits == num):
        print(num, end = ' ')