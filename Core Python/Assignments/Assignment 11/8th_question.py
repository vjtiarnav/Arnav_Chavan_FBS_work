# Print 1 to 100 in snakes and ladder pattern.
final_list = []

for i in range(0,10):
    num_list = []
    for j in range(i*10+1,i*10+11):
        num_list.append(j)
    if(i % 2 != 0):
        num_list.reverse()
        final_list.append(num_list)
    else:
        final_list.append(num_list)
            
final_list.reverse()
print(final_list)