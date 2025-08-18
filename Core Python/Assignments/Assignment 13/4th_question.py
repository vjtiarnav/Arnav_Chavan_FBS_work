# Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

# Approach 1

def createDict(n):
    
    dict1 = {}
    for i in range(1,n+1):
        dict1[i] = i*i
        
    return dict1
    
n = int(input("Enter a number: "))
resultDict = createDict(n)
print(resultDict)

# Approach 2

def createDict(n):

    dict1 = {x:x*x for x in range(1,n+1)}
    return dict1
    
n = int(input("Enter a number: "))
resultDict = createDict(n)
print(resultDict)