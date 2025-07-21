'''
Write a program to accept basic salary of n employees (n should be accepted from the user).
If basic salary is below 20000 then da = 10%, ta = 12% and hra = 15%.
Otherwise da = 15%, ta = 18% and hra = 20%.
Based on this calculate the total salary of each employee and also the total salary of all employees
'''

n = int(input("Enter number of employees: "))

total_salary = 0

for i in range(1,n+1):
    basic_salary = float(input(f"\nEnter the basic salary of employee {i}: "))
    
    if(basic_salary < 20000):
        da = basic_salary*0.1
        ta = basic_salary*0.12
        hra = basic_salary*0.15
        
    else:
        da = basic_salary*0.15
        ta = basic_salary*0.18
        hra = basic_salary*0.2
        
    emp_salary = basic_salary + da + ta + hra
    total_salary += emp_salary
    
    print(f"The total salary of employee {i} is Rs.{emp_salary}")
 
print("\n--------------------------------------------------------")   
print(f"The total salary of {n} employees is {total_salary}")
        