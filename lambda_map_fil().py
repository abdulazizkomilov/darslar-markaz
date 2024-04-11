# import math

# def daraja(x):
#     ifoda = x * x
#     return ifoda

# daraja_2 = lambda x: x * x
# print(daraja_2(5))

# uzunlik = lambda pi, r: 2*pi*r
# print(uzunlik(math.pi, 5))

# sonlar_3 = lambda x, y, z: x * y * z

# print(sonlar_3(3, 4, 5))




# # def kbvadrat(x, y):

# kvadrat = lambda x, y: x ** y
# print(kvadrat(9, 8))


# def daraja(n):
#     return lambda x: x ** n

# kvadrat = daraja(2)
# kub = daraja(3)
# four = daraja(4)
# on = daraja(10)

# print(kvadrat(4))
# print(kvadrat(9))
# print(kub(6))
# print(four(16))
# print(on(22))

# # print(kvadrat(38))
# besh_dj = daraja(5)
# print(besh_dj(38))
# print(f"3-ning kvadrati {kvadrat(3)} ga, " 
#       f"kubi {kub(3)} ga teng")



# from math import sqrt, factorial  # sqrt - kvadrat ildiz

# sonlar = list(range(11))  # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(factorial, sonlar)) 
# print(ildizlar)



# map(funksiya, qiymatlar) -- list(map()) 
# qiymatlar ichidagi har bir son uchun 
# ishlaydi

# print(ildizlar)


names = ['ali', 'vali', 'olim', 'hakim', 'husan', 'hasan']

# def ism_upper(arr):
#     ismlar = []
#     for ism in names:
#         ismlar.append(ism.upper())
#     return ismlar
# print(ism_upper(names))

# print(list(map(lambda ism: ism.upper(), names)))







# def daraja(x):
#     """Berilgan sonning kvadratini q f"""
#     return x*x

# sonlar = list(range(11))

# print(list(map(lambda x: x*x, sonlar)))



sonlar = list(range(11))

# def son_t(x):
#     if x % 2 == 1:
#         return x

# print(list(map(son_t, sonlar)))
      

# print(list(map(son_t, sonlar)))



# sonlar = list(range(11))

# kvadratlar = list(map(lambda x: x * x, sonlar))
# print(kvadratlar)


# a = [4, 5, 6]
# b = [7, 8, 9]   

# # # c = [3, 7, 2]
# # # a+b+c

# a_plus_b = list(map(lambda x, y: x + y, a, b))
# print(a_plus_b)




import random as r

sonlar = r.sample(range(100), 10)  # 0-99 oralig'ida 10 ta tasodifiy sonlar
print(sonlar)


# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
#     return x % 2 == 0


# print(list(filter(juftmi, sonlar)))




# juft_sonlar = list(filter(lambda x: x % 2 == 1, sonlar))
# print(juft_sonlar)


import random as r

mevalar1 = ["olma", "limon", "sabzi", 
            "kivi", "olcha", "olxuri", 
            "sarimsoq", "salim"]

# filtered_fruits = list(filter(lambda meva: meva.startswith('s'), mevalar1))
# print(filtered_fruits)






# mevalar2 = list(filter(lambda meva: len(meva) <= 5, mevalar1))
# print(mevalar2)

# print(list(filter(lambda meva: (meva.startswith("s") and meva.endswith("i")), mevalar1)))




# import random as r

# sonlar = r.sample(range(100), 10)

# print(sonlar)

# juft = [son for son in sonlar if son%2==0]; print(juft)

# toq = [son for son in sonlar if son%2!=0]; print(toq)

# for son in sonlar:
#     if son%2==0:
#         print(son)





# import random as r 

# son = r.randint(0, 100) # 0 va 100 oralig'ida tasodifiy son
# print(son)


# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
# print(ism)
# print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz


# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))


# import random as r

# x = list(range(11))   # x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya
# print(x)
# r.shuffle(x)
# print(x)
# r.shuffle(x)
# print(x)



# import random as r

# son1 =r.randint(0, 10)
# son2 =r.randint(0, 10)
# son3 =r.randint(0, 10)
# natija = int(input(f"Hisoblang:\n{son1} + {son2} + {son3} = "))
# n = son1+son2+son3
# if natija == n:
#     print(f"To'g'ri. Javob: {n}")
# else:
#     print(f"Noto'g'ri. Javob: {n}")






# Amallardan birini tanlang: " + | - | x | : "
# >>> x









