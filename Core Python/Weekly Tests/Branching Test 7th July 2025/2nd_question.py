num = int(input("Enter a three digit number: "))
originalNum = num

thirdDigit = num % 10
num = num // 10
secondDigit = num % 10
firstDigit = num // 10

if(firstDigit == 2*secondDigit and firstDigit == 0.5*thirdDigit):
    print("Yes, you have done it.")
else:
    print("Please try next time.")