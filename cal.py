data = 1
print("Yan:")
print(" Sun Mon Tue Wed Thu Fri Sat")
for week in range(4):
    for day in range(7):
        print(f"{data:4d}", end='')
        data+=1
    print('')