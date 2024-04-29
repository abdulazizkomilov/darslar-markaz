# try-except

# list_1 = [2, 3, 4, 5, 6, 7]

# try:
#     son = int(input("son: "))
#     print(list_1(son))
# except IndexError:
#     print('Index xatoligi')
# except TypeError:
#     print('Murojat qilish xatoligi')
# except AttributeError:
#     print('AttributeError qilish xatoligi')
# except ValueError:
#     print("Notugri malumot kiritildi")


# print('hi')



# list_1 = [2, 3, 4, 5, 6, 7]
# try:
#     print(list_1(8))
# except:
#     print('Xatolig')
# print('dsadfasd ')




# # Xatolar
# yosh = int(input("Yoshingizni kiriting: "))
# print(f"Siz {2024-yosh} yilda tug'ilgansiz")
# print('hi')







# # try-except
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
#     print(f"Siz {2024-yosh} yilda tug'ilgansiz")
# except: 
#     print("Butun son kiritmadingiz")
# print('hi')





# # try-except-else
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2023-yosh} yilda tug'ilgansiz")
    
# print('dastur t')





# x, y = 3, 10
# try:
#     print(y/(x-3))
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# except Exception as e:
#     print(f"{e}")





# mevalar = ['olma','anor','anjir','uzum']
# for ind, meva in enumerate(mevalar):
#     print(f"{ind+1}: {meva}", end=' ')
    
# a = int(input("\nindex kiriting: "))
# index = a - 1
# try:
#     if len(mevalar) <= index:
#         mevalar[index]
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")
# else:
#     print(mevalar[index])




# data = {
#         }

# kalit = input("kalit k: ")
# qiymat = input("qiymat k: ")
# data[kalit] = qiymat

# print(data)








# data = {"username":"admin",
#         "status":"owner",
#         "email":"admin@uz.dev",
#         "phone":"99897123456"}

# print('Mavjud keylar: ')
# for i in data:
#     print(i, end=", ")

# key = input("\nKeylardan birini kiriting: ")
# try:
#     print(f'Foydalanuvchi: {data[key]}')
# except KeyError:
#     print("Bunday kalit mavjud emas")


# sonlar2 = [99,5,4,7,8,0,1,2,3,9,33]

# sonlar = [9,2,5,7,4,6]
# OUT:
#     [2,4,5,6,7,9]


# filename = "data.txt" # bunday fayl mavjud emas
# with open(filename) as f:
#     text = f.read()



filename = "data.txt" # bunday fayl mavjud emas
try:
    with open(filename) as f:
        text = f.read()
except FileNotFoundError:
    print(f"Kechirasiz, {filename} fayli mavjud emas. Boshqa fayl tanlang.")
else:
    print(text)




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
#     x=20/n
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



# try:
#     x = int(input("son kiriting: "))
#     y = int(input("yana son kiriting: "))
#     print(x, "/", y, "=", x / y)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# except ValueError:
#     print("Bu kasir son butun son k")
# except Exception as error:
#     print(f"{error} Xato yuz berdi!")
