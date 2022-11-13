son = input("son kiriting>>>  ")

def son_top(num):
    summa = 0 
    for x in range(len(son)):
        summa =  summa + int(son[x])
    return summa

print(son_top(son))

