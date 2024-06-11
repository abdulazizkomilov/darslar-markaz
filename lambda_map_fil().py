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



# kvadrat = lambda x, y: x ** y
# print(kvadrat(2, 3))





# def daraja(n):
#     return lambda x: x ** n

# kv = daraja(2)
# kub = daraja(3)
# four = daraja(4)
# besh = daraja(5)

# print(kv(4))
# print(kv(9))
# print(kub(6))
# print(four(16))
# print(besh(12))




# # print(kvadrat(38))
# besh_dj = daraja(5)
# print(besh_dj(38))
# print(f"3-ning kvadrati {kvadrat(3)} ga, " 
#       f"kubi {kub(3)} ga teng")



# from math import sqrt # sqrt - kvadrat ildiz


# print(list(map(sqrt, list(range(11)))))


# map(funksiya, qiymatlar) -- list(map()) 
# qiymatlar ichidagi har bir son uchun 
# ishlaydi





# print(ildizlar)


# names = ['ali', 'vali', 'olim', 'husan', 'hasan']

# def ism_upper(arr):
#     ismlar = []
#     for ism in names:
#         ismlar.append(ism.upper())
#     return ismlar
# print(ism_upper(names))




# print(list(map(lambda x: x.upper(), names)))







# def daraja(x):
#     """Berilgan sonning kvadratini q f"""
#     return x*x

# sonlar = list(range(11))

# print(list(map(lambda x: x*x, sonlar)))



# sonlar = list(range(11))

# def son_t(x):
#     if x % 2 != 0:
#         return x

# print(list(map(son_t, sonlar)))
      




# sonlar = list(range(11))

# kvadratlar = list(map(lambda x: x % 2 != 0, sonlar))
# print(kvadratlar)




# a = [4, 5, 6]
# b = [7, 8, 9]   
# c = [3, 7, 2]


# a_plus_b = list(map(lambda x, y, z: x + y + z, a, b, c))
# print(a_plus_b)






# import random as r

# sonlar = r.sample(range(100), 5)  # 0-99 oralig'ida 10 ta tasodifiy sonlar
# print(sonlar)


# print(list(filter(lambda x: x % 2 == 0, sonlar)))


# mevalar = ["olma", "limon", "sabzi", 
#             "kivi", "olcha", "olxuri", 
#             "sarimsoq"]

# f_fruits = list(filter(lambda meva: meva.startswith('o'), mevalar))
# print(f_fruits)





# mevalar2 = list(filter(lambda meva: len(meva) > 5, mevalar))
# print(mevalar2)





# print(list(filter(lambda meva: (meva.startswith("o") and meva.endswith("a")), mevalar1)))




# import random as r
 
# sonlar = r.sample(range(100), 10)


# juft = [son for son in sonlar if son%2==0]; print(juft)


# toq = [son for son in sonlar if son%2!=0]; print(toq)


# for son in sonlar:
#     if son%2==0:
#         print(son)





import random as r 

son = r.randint(0, 100) # 0 va 100 oralig'ida tasodifiy son
print(son)



ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz


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

# son1 = r.randint(1, 10)
# son2 = r.randint(15, 24)
# natija = int(input(f"Hisoblang:\n{son1} + {son2} = "))
# n = son1+son2
# if natija == n:
#     print(f"To'g'ri. Javob: {n}")
# else:
#     print(f"Noto'g'ri. Javob: {n}")


# Amallardan birini tanlang: " + | - | x | : "
# >>> x









