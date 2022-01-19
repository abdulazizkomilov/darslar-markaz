# import math

# def nom(argument):
#     return ifoda
# lambda x: x*x
# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))
# def kbvadrat(x, y):

# kvadrat = lambda x, y : x ** y
# print(kvadrat(3, 2))


# def daraja(n):
#     return lambda x: x ** n


# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga, " f"kubi {kub(3)} ga teng")



# from math import sqrt  # sqrt - kvadrat ildiz

# sonlar = list(range(11))  # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)

# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x

# print(list(map(daraja2,sonlar)))

# kvadratlar = list(map(lambda x: x * x, sonlar))
# print(kvadratlar)


# a = [4, 5, 6]
# b = [7, 8, 9]       
# a_plus_b = list(map(lambda x, y: x + y, a, b))
# print(a_plus_b)

# ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda matn:matn.upper(),ismlar)))

import random as r

sonlar = r.sample(range(100), 10)  # 0-99 oralig'ida 10 ta tasodifiy sonlar
# print(sonlar)


# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
#     return x % 2 == 0


# juft_sonlar = list(filter(juftmi,sonlar))
# print(juft_sonlar)

# juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
# print(juft_sonlar)


mevalar = ["olma", "anor", "anjir", "shaftoli", "o'rik", "tarvuz", "qovun", "banan"]
# harf = "b"
# mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))
# print(mevalar_b)

# mevalar2 = list(filter(lambda meva: len(meva) <= 5, mevalar))
# print(mevalar2)

# print(list(filter(lambda meva: (meva.startswith("a") and meva.endswith("r")), mevalar)))

sonlar = r.sample(range(100),10)
juft = [son for son in sonlar if son%2==0]; print(juft)


# f1 = lambda x: x * 10
# print(f1(10))

# f2 = lambda x, y: x * y
# print(f2(5, 4))

# from random import sample
# from math import sqrt

# x = list(range(0, 1001))
# y = sample(x, k=10)
# print(y)

# ildizlar = list(map(lambda n: sqrt(n), y))
# print(ildizlar)

# toq_sonlar = list(filter(lambda n: n % 2, y))
# print(toq_sonlar)


# def tubmi(x):
#     if x % 2 == 0 or x < 2:
#         return False  # Son juft yoki 2 dan kichik bo'lsa
#     if x == 2 or x == 3:
#         return True  # Son 2 yoki 3 bo'lsa
#     for i in range(3, x, 2):
#         if x % i == 0:
#             return False
#     return True


# tub_sonlar = list(filter(tubmi, range(100)))
# print(tub_sonlar)