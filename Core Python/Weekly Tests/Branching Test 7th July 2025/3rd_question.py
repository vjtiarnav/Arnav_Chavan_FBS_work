import math

radius = 20
length = 50 
breadth = 40

perimeter = (math.pi*radius) + 2*length + breadth

costOfWire = 35

totalCost = perimeter*costOfWire*5

print(f"The total cost of fencing the field 5 times using a barbed wire is Rs.{totalCost:.2f}")