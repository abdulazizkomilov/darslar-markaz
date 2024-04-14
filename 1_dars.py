# PYTHON 3


# print("Hello world!")

# print('Salom!')
# print("Assalomu alaykum.")


# print(56 + 6)

# print(877)



# input() foydalanuvchidan malumot so'rash

# name = input('Ism kiriting: ')
# print(f"Salom {name}")

# yosh = input("Yosh kiriting>>>  ")
# print(f"Sizning yoshingiz {yosh} da")


# yosh = int(input("Yoshingizni kiriting>>>  "))
# print(f"{2024 - yosh} da")




# data types - malumotlar turi

# a = 'salom'     # matn - string  - str()
# b = 45          # son  - integir - int()
# c = '45'
# print(type(c))
# print(type(a))
# print(type(b))

# type(x) - malumot qaysi data typega te..








# yosh = int(input("Yoshingizni k>>>  "))
# print(f"Sizning yoshingiz: {yosh} da")

# print(2024 - yosh)




# a = 'olim'
# print(a)

# b = 5
# c = 16
# d = 9
# yigindi = b + c
# bulinma = yigindi / d
# print(yigindi)
# print(bulinma)




# input() - {foydalanuvchidan m s}
# input() doim string {matn q q}
# str() - string  {matn}
# int() - integir  {son}
# float() - float  {kasr sonlar}
# type(x) - qaysi dataga tegishliligini aniq




# ism = input("Ismingizni kiriting:  ")
# print("Xush kelibsiz -", ism)
 

# a = int(input("a sonni kirit "))
# b = int(input("kiyingi sonni kiriting "))

# print(f"{a} + {b} = {a + b}")



# son = int(input("istalgan son kiriting: "))
# print(f"{son}ning kv {son**2}ga teng")







# a = int(input("son kirit>>> "))
# b = int(input("sonni kirit>>> "))
# c = int(input("son kiriting>>> "))
# a_b = a + b
# natija = a_b - c
# print(f"{a} + {b} = {a_b}")
# print(natija)




# name = input("Assalomu alaykum foydalanuvchi isminzgizni kiriting: ")
# print('Assalomu alaykum', name, 'dasurimizga xush kelibsiz!')



# son1 = 10
# son2 = 33
# print("a = ", son1)
# print("b = ", son2)
 



# t_yil = int(input("tugulgan yilingizni k:  "))
# print("sizning yoshingiz ", 2024 - t_yil, "da")



# a = 5
# b = 6
# c = 'assalomu alaykum'

# print("c =", c)
# print("b =", b)
# print("a =", a)

# name = "Ali Olimov"
# age = 20

# print(name, "yoshim", age, "da", )



# ism = input("Ismingizni kiriting>>>  ")
# yosh = int(input("Yoshingni kiriting>>>  "))
# print(ism, "s t yilingiz ", 2024 - yosh, "-yil da")
#          # sizning tugulgan

# str() - string  {matn}
# int() - integir  {son}

# a = "olim hakimov jamol ogli"
# b = 'KLdfJDFdadfNsadfsaLKJHHKLJK'

# print(a)
# print(a.capitalize())
# print(a.title())
# print(b.upper())
# print(b.lower())
# # .capitalize() - bitta so'zni bosh harfini
# # .title() - har bir so'zni bosh harfini 
# # .upper() - barcha harflarni katta qiladi
# # .lower() - barcha harflarni kichik qiladi

# ism = "ali jamolov"

# print(ism.upper())





# Example: input("Ismingizni kiriting:  ")
# foydalanuvchidan consolda malumot 
# so'raydi va doim input() matn-str()
# qabul qiladi  

# input() ni songa aylantirish uchun oldiga
# int(input("...")) qo'yiladi. int() - bu son

# name = input("Ismingizni kiriting: ")
# print(name)
# print("Salom", name.title())


# age = int(input("Yoshingizni kiriting: "))
# print("Sizning tugulgan yilingiz", 2024 - age)




# + - / *
# a = 21
# b = 6
# natija = a + b
# print(a, '+', b, '=', natija)

# son4 = a - b
# print(a, "-", b, "=", son4)

# a = 2
# b = 3
# natija = a * b
# print(a, "x", b, "=", natija)


# a = int(input('a sonni kiriting:  '))
# b = int(input("b sonni kiriting:  "))
# print(a, ":", b, "=", a / b)



# # % // **, <, >,
# son1 = 10
# son2 = 3              # 3,    1 q

# print(son1 / son2)    # 3.3333
# print(son1 % son2)    # 1 qoldiq
# print(son1 // son2)   # 3 butun qismi
# print(son2 ** 2)      # 9 darajasi



    
    
# f" ..., {son1+son2}  ...? {son2} "

# son1 = 10
# son2 = 3 

# butun_q = son1 // son2
# qoldiq_q = son1 % son2
# # f " " - f string
# print(f"{son1} : {son2} = {butun_q} butun qismi, {qoldiq_q}, qoldiq qismi.")


# a = 22
# b = 54
# print(a > b) #xato -- False
# print(a < b) #tugri - True

# data_type - malumotlar turi
# str() - string  {matnlar} 'salom', "hi" 
# int() - integir  {sonlar}  1, 2, 4, 6, 0, -1, -654
# float() - kasr sonlar  7.6, 6.09, 54.25
# bool() - True, False
# input() - {foydalanuvchidan malumot suraydi}
# input() doim string {matn qabul qilmoq}
# type(x) - qaysi dataga tegishliligini aniq
# .capitalize() - bitta so'zni bosh harfini
# .title() - har bir so'zni bosh harfini 
# .upper() - barcha harflarni katta qiladi
# .lower() - barcha harflarni kichik qiladi




# # # ==, !=
# son = 10 == 6 # f
# son2 = 27 != 26 # t
# son3 = 6 == 6 # t
# print(son)
# print(son2)
