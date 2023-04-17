# # Xatolar
# yosh = input("Yoshingizni kiriting: ")
# print(f"Siz {2021-yosh} yilda tug'ilgansiz")

# # try-except
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
#     print(f"Siz {2022-yosh} yilda tug'ilgansiz")
# except ValueError:
#     print("Butun son kiritmadingiz")
# # # try-except-else
# print("Dastur Tugadi!")

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2022-yosh} yilda tug'ilgansiz")

# x, y = 3, 10
# try:
#     print(y/(x-3))
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")

# mevalar = ['olma','anor','anjir','uzum']
# a = int(input("index kiriting: "))
# index = a - 1
# try:
#     if len(mevalar) <= index:
#         mevalar[index]
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")
# else:
#     print(mevalar[index])

# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":99897123456}

# key=input("Biror kalit soz kiriting: ")
# try:
#     print(f'Foydalanuvchi: {user[key]}')
# except KeyError:
#     print("Bunday kalit mavjud emas")




# filename = "data.txt" # bunday fayl mavjud emas
# with open(filename) as f:
#     text = f.read()

# filename = "pi.txt" # bunday fayl mavjud emas
# try:
#     with open(filename) as f:
#         text = f.read()
#         print(text)
# except FileNotFoundError:
#     print(f"Kechirasiz, {filename} fayli mavjud emas. Bosh fayl tanlang.")

# n = input("Butun son kiriting: ")
# n = int(n)
# x=20/n
# print(x)

# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x=20/n
# except ValueError:
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     x=20%n
#     print(x)

# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break

# print(f"Siz {2021-yosh} yilda tug'ilgansiz")

# print("x/y hisoblovchi dastur")
# while True:
#     x = input("x ni kiriting: ")
#     if x.isdigit():
#         x = int(x)
#     else:
#         print("Bu son emas!")
#         continue

#     y = input("y ni kiriting: ")
#     if y.isdigit():
#         y = int(y)
#     else:
#         print("Bu son emas!")
#         continue

#     if y == 0:
#         print("y 0 bo'lishi mumkin emas!")
#         continue
#     else:
#         print(x, "/", y, "=", x / y)
#         break

# # try:
# #     x = int(input("son kiriting: "))
# #     y = int(input("yana son kiriting: "))
# #     print(x, "/", y, "=", x / y)
# # except ZeroDivisionError:
# #     print("0 ga bo'lib bo'lmaydi")
# # except ValueError:
# #     print("Bu son emas")
# # except:
# #     print("Xato yuz berdi!")


