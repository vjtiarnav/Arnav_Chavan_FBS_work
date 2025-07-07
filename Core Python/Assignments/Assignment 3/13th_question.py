'''
Write a program to input electricity unit charges and calculate total electricity bill
according to the given condition:
    For first 50 units Rs. 0.50/unit
    For next 100 units Rs. 0.75/unit
    For next 100 units Rs. 1.20/unit
    For unit above 250 Rs. 1.50/unit
    An additional surcharge of 20% is added to the bill
'''
units = float(input("Enter the number of units consumed: "))

if units <= 50:
    bill = units * 0.5

elif units <= 150:
    bill = 50 * 0.5
    bill += (units - 50) * 0.75

elif units <= 250:
    bill = 50 * 0.5
    bill += 100 * 0.75
    bill += (units - 150) * 1.20

else:
    bill = 50 * 0.5
    bill += 100 * 0.75
    bill += 100 * 1.20
    bill += (units - 250) * 1.50

# Add 20% surcharge
bill += bill * 0.20

print(f"The bill is Rs.{bill:.2f}")
