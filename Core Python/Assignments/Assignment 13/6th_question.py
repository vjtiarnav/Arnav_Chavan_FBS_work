# Python Program to Multiply All the Items in a Dictionary

def multiply_items(my_dict):
    product = 1
    for key in my_dict:
        product *= my_dict[key]

    return product

my_dict = {'a':10,'b':20,'c':30}
ans = multiply_items(my_dict)
print(f"The multiplication of the items in {my_dict} is {ans}")