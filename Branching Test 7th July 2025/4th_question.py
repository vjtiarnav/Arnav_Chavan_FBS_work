height = float(input("Enter the height of each wall (in meters): "))
width = float(input("Enter the width of each wall (in meters): "))
cost_per_sqm = float(input("Enter the cost of painting per square meter: "))

area_one_wall = height * width

total_area = 4 * area_one_wall

total_cost = total_area * cost_per_sqm

print(f"\nTotal area to be painted: {total_area:.2f} square meters")
print(f"Total cost of painting: ₹{total_cost:.2f}")
