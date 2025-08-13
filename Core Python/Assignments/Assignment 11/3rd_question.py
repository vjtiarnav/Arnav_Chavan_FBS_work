# Python Program to Sort the List According to the Second Element in Sublist

n_list = [[11,5,7],[9,3,2],[6,3,5],[7,8,1]]

n = len(n_list)

for i in range(n):
    for j in range(0,n-i-1):
        if n_list[j][2] > n_list[j+1][2]:
            n_list[j],n_list[j+1] = n_list[j+1],n_list[j]

print(n_list)