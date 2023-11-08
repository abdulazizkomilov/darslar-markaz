import random as r

# # randint()
# son = r.randint(0,50)
# print(son)

# # # choice()
# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar)
# print(ism)

# print(r.choice(ism))
# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))

# # shuffle()
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)


# ismlar = ['zarnigor', 'muslima', 'samandar', 'og`abek', 'ramazon']

# print(f'ismlar uzunligi {len(ismlar)}')
# print(ismlar)

# r.shuffle(ismlar)
# print(ismlar)
# print(r.choice(ismlar))

# son1 = r.randint(1,50)
# son2 = r.randint(11, 21)
# print(f"Javobni toping: \n{son1} + {son2} = ?")
# javob = int(input(">>>  "))
# if javob == son1+son2:
#     print('Tugri')
# else:
#     print('Xato')


amallar = {
    1:'+', 
    2:'-',
    3:'x',
}
son1 = r.randint(1,10)
son2 = r.randint(1, 10)
son = r.randint(1,3)
amal = amallar[son]
print(f"Javobni toping: \n{son1} {amal} {son2} = ?")
javob = float(input(">>>  "))
if amal == '+':
    if javob == son1+son2:
        print('Tugri')
    else:
        print('Xato')
if amal == '-':
    if javob == son1-son2:
        print('Tugri')
    else:
        print('Xato')
if amal == 'x':
    if javob == son1*son2:
        print('Tugri')
    else:
        print('Xato')







