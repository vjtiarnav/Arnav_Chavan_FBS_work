# Write a program to calculate Compound Interest

principal = int(input("Enter the principal amount: "))
rateOfInterest = float(input("Enter the rate of interest: "))
years = int(input("Enter the number of years: "))

compoundInterest = principal*(1+(0.01*rateOfInterest))**years

print(f"The compound interest is {compoundInterest}")
print(f"The total amount is {compoundInterest+principal}")