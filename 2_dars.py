# # Constanta
# # type()
# PI = 3.14
# G = 9.81
# A = 3
# OYLIK = 300_000


# import math

# print(math.pi)

# a = 9
# b = 49

# print(math.sqrt(b)) # ildizdan chiqaradi

# print(math.ceil(45.6)) # katta yaqiniga 46 

# print(math.floor(45.67)) # kichik yaqiniga 45

# print(math.sin(90))  #sonning sin si

# print(math.factorial(1000))  # 1*2*3*4*5

# print(math.log(144, 5))  #(5*5*5) == 5**3

# print(math.cos(180))



# list -- ro'yxat
#  index         0       1      2           3         4|-2          5|-1
# qurulmalar = ["telfon", 'TV', 'wifi', 'sichqoncha', 'headphones', 'lamp']
# print(qurulmalar[1])
# print(qurulmalar[-1])


# # ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# ismlar = ["ali", "olim", "vali"]

# # # Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
# print(f"""Salom {ismlar[0].upper()}, 
# {ismlar[1].title()}, {ismlar[-1].title()} 
# ishlaring yaxshimi?""")


# f_name = input("ism familya kiriting:  ")
# year = int(input("tug yil kiriting:  "))
# address = input("manzil:  ")
# phone = int(input("tel:  "))
# print(f"""Salom {f_name.title()}, 
# sizning yoshingiz {2023-year}da siz, 
# manzil: {address.capitalize()},
# tel: {phone}""")


# print(f"  ")   # f - string

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).

# sonlar = [22, -58.2, 34.0, 67, 1983, 123_450_001, 112.4]
# print(sonlar)
# print(sonlar[-1])

# sonlar[0] = sonlar[0] + sonlar[-1]
# sonlar[1] = -67.8
# sonlar[4] = sonlar[4] + 40
# sonlar[3] = 77
# print(sonlar)
# del sonlar[5]  # delete - o'chirish
# del sonlar[0]
# print(sonlar)


# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga 
# # chaqirmoqchi bo'lgan do'stlaringizni kiriting.

friends = []
friends.append("John")
friends.append("Alex")
friends.append("Danny")
friends.append("Sobirjon")
friends.append("Vanya")
print(f"To`liq list: {friends}")

# # # Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
friends.remove("John")
friends.remove("Alex")
del friends[-1]
print(f"Kelganlar-{friends}")

# talaba = ['jon', 'vaniya', 'kamol']
# print(talaba)
# talaba.append("Hasan")
# talaba.insert(0, "Husan")
# talaba.insert(2, "Ivan")

# print(talaba)
# print(len(talaba))


# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. 
# .pop() va .append() metodlari yordamida mehmonga kelgan 
# do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

# friends = []
# friends.append("John")
# friends.append("Alex")
# friends.append("Danny")
# friends.append("Sobirjon")
# friends.append("Vanya")
# print(friends)

# mehmonlar = []
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(0))
# mehmonlar.insert(2, friends.pop(0))
# print("\nKelgan mehmonlar: ", mehmonlar)



