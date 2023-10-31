import math

# def daraja(x):
#     ifoda = x * x
#     return ifoda



# daraja_2 = lambda x, y: x ** y  # nomsiz funksiya lambda
# print(daraja_2(5, 3))


# uzunlik = lambda pi, r: 2*pi*r
# print(uzunlik(math.pi, 5))



# def kbvadrat(x, y):

# kvadrat = lambda x, y : x ** y
# print(kvadrat(3, 2))


# def daraja(n):
#     return lambda x: x ** n


# kvadrat = daraja(2)
# kub = daraja(3)
# turt = daraja(4)
# on = daraja(10)

# print(kvadrat(6))
# print(kub(3))
# print(turt(8))
# print(on(100))


# # print(kvadrat(38))
# besh_dj = daraja(5)
# print(besh_dj(38))
# # print(f"3-ning kvadrati {kvadrat(3)} ga, " f"kubi {kub(3)} ga teng")



# from math import sqrt  # sqrt - kvadrat ildiz

# sonlar = list(range(11))  # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(sqrt, sonlar)) 

# # map(funksiya, qiymatlar) -- list(map()) qiymatlar ichidagi 
# # har bir son uchun ishlaydi

# print(ildizlar)




# def daraja(x):
#     """Berilgan sonning kvadratini q f"""
#     return x*x

# sonlar = list(range(11))

# print(list(map(daraja, sonlar)))



# sonlar = list(range(11))

# kvadratlar = list(map(lambda x: x * x, sonlar))
# print(kvadratlar)



# a = [4, 5, 6]
# b = [7, 8, 9]   
    
# a_plus_b = list(map(lambda x, y: x + y, a, b))
# print(a_plus_b)



# ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda matn:matn.upper(), ismlar)))






# import random as r

# sonlar = r.sample(range(100), 10)  # 0-99 oralig'ida 10 ta tasodifiy sonlar
# print(sonlar)

# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
#     return x % 2 == 0

# juft_sonlar = list(filter(juftmi, sonlar))
# print(juft_sonlar)

# juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
# print(juft_sonlar)



# mevalar = ["olma", "anor", "anjir", "shaftoli", "o'rik", "tarvuz", "qovun", "banan"]
# # mevalar_b = list(filter(lambda meva: meva.startswith('a'), mevalar))
# # print(mevalar_b)


# mevalar2 = list(filter(lambda meva: len(meva) <= 5, mevalar))
# print(mevalar2)

# print(list(filter(lambda meva: (meva.startswith("s") and meva.endswith("i")), mevalar)))


# import random as r

# sonlar = r.sample(range(100),10)
# juft = [son for son in sonlar if son%2==0]; print(juft)

# # for son in sonlar:
# #     if son%2==0:
# #         son



# import random as r 

# son = r.randint(1,11) # 0 va 100 oralig'ida tasodifiy son
# print(son)


# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
# print(ism)
# print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz


# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))


# x = list(range(11))   # x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya
# print(x)
# r.shuffle(x)
# print(x)


