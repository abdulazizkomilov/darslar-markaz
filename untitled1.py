b = [2, 6, 4, 8, 1, 0, 5, 3, 7]

# 0: ind
# 1, 6, 4, 8, 2, 0, 5, 3, 7

# 1: ind
1, 4, 6, 8, 2, 0, 5, 3, 7

# 2: ind
1, 4, 6, 8, 2, 0, 5, 3, 7



def sort_list(l: list) -> list:
    
    p = 0
    cur = 1
    l[p], l[cur]=l[cur], l[p]
    return tuple(l)

print(sort_list(b))














