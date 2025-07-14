# WAP to check if given number is a Strong Number.

isnotStrong = True

while(isnotStrong):
    n = int(input("Enter a number: "))
    originalNum = n
    sumofFact = 0
    
    while(n > 0):
        digit = n % 10
        fact = 1
        for i in range(1,digit+1):
            fact *= i
        sumofFact += fact
        n = n // 10
        
    if(sumofFact == originalNum):
        print(f"{originalNum} is a Strong Number")
        isnotStrong = False
    else:
        print(f"{originalNum} is not a Strong Number\n")
        
    
