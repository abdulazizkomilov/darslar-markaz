# son = int(input("Juft son kiriting: "))
# if son % 2 != 0:
#     print("Bu son juft emas.")
# else:
#     print("Rahmat!")
    
    
# # #2
# yosh = int(input("Yoshingiz nechida? "))

# if yosh <= 4 or yosh >= 60: # agar
#     narh = 0
# elif yosh < 18:    #aks holda agar 
#     narh = 10000
# else:               #aks holda
#     narh = 20000
    
# print(f"Chipta {narh} so'm")


# #3
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x == y:
#     print(f"{x}={y}")
# elif x < y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")


# #4
# mahsulotlar = [
#     "un",
#     "yog'",
#     "sovun",
#     "tuxum",
#     "piyoz",
#     "kartoshka",
#     "olma",
#     "banan",
#     "uzum",
#     "qovun",
# ]

# savat = []
# # for n in range(5):
# #     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else:
#     print("Savatingiz bo'sh")
    
    
    
# #4
# mahsulotlar = [
#     "un",
#     "yog'",
#     "sovun",
#     "tuxum",
#     "piyoz",
#     "kartoshka",
#     "olma",
#     "banan",
#     "uzum",
#     "qovun",
# ]


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
    
# # 5
# users = ["alisher1983", "aziza", "yasina", "umar"]

# login = input("Yangi login tanlang: ")

# if login in users:
#     print("Login band, yangi login tanalng!")
# else:
#     print("Xush kelibsiz!")
    
    
# # # 6
# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2, 11):
#     if not (son % n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

# 1
# for x in range(1,11):
#     print(x, end=(" "))


# # 2
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for x in sonlar:
#     print(x, end=(" "))


# # 3
# narsalar = ['olma', 43, 'un', 'qalam', 6, 90, 'yilkan']

# for a in narsalar:
#     print(a, end=(", "))
    

# # # 4
# til = input("Tilni tanlang: uz/en/ru ? ")

# if til == 'uz':
#     print("Assalomu alaykum")
# elif til == 'en':
#     print("HELLO")
# else:
#     print("uz/en lardan birini tanlang")

# # ikkita tasodifiy son
# from random import randint

# a = randint(1, 11)
# b = randint(1, 11)

# c = int(input('{} + {} = '.format(a, b)))

# if c == (a + b):
#     print("To`g`ri! :)")
# else:
#     print("Xato! :(")
 
# from random import randint   
# print("Amallardan birini tanlang: ")
# a = ["ayirish", "bo'lish", "qo'shish"]

# son = 1
# for b in a:
#     print(son, "-", b, end=("\n"))
#     son += 1
    
# savol = input("Amal raqamini kiriting. >>>  ")
# if savol == "1":
#     a = randint(1, 11)
#     b = randint(1, 11)
#     print("Misolni javobini kiriting:")
#     c = int(input('{} - {} = '.format(a, b)))
#     if c == (a - b):
#         print("To`g`ri! :)")
#     else:
#         print("Xato! :(")
# elif savol == "2":
#     print("bo'lish")
# elif savol == "3":
#     print("qo'shish")

# # yil 
# a = int(input("Yilni kiriting >>> "))

# if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
#     print("Kabisa yil")
# else:
#     print("Kabisa yil emas")


# # oylar
# oy = int(input("oy>>> "))

# oylar = ['yan', 'fev', 'mart', 'apr', 'may', 
#           'iyn', 
#           'iyl', 
#           'avg', 
#           'sep', 
#           'okt', 
#           'nov',
#           'dek']

# print(f"{oylar[oy-1]}")
