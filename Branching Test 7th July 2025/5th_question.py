n = int(input("Enter the number of products purchased: " ))

productCost = []
amount = 0

for i in range(n):
    cost = float(input(f"Enter the cost of product {i+1}:"))
    productCost.append(cost)

for i in productCost:
    amount = amount + i

totalBill = amount + (0.18*amount)

print(f"The total bill of {n} products is Rs.{totalBill}")
