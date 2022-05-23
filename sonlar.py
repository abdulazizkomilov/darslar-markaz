a = input(">>>  ")
try:
    if float(a) % 2 == 0:
        print('son')
    else:
        print('float')
except ValueError:
    print("harf")