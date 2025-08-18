# Python Program to Calculate the Length of a String Without Using a Library Function

def calc_length(str1):
    count = 0
    for ch in str1:
        count += 1

    return count

str1 = input("Enter a string: ")
length = calc_length(str1)
print(f"The length of \"{str1}\" is {length}")