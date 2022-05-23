a_list = [4, 2, 5, 1, 3]


for i in range(0, len(a_list)):
    print(i)
    for j in range(i + 1, len(a_list)):
        
        if a_list[i] >= a_list[j]:
            
            a_list[i],a_list[j] = a_list[j],a_list[i]
            

print(a_list)
