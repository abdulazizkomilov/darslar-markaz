# # Constanta
# # type()
# PI = 3.14
# G = 9.81
# A = 3
# OYLIK = 300_000


# import math

# a = 9
# b = 49

# print(math.pi)

# print(math.sqrt(b)) # √49 ildizdan chiqaradi

# print(math.ceil(45.6)) # katta yaqiniga 46 

# print(math.floor(45.67)) # kichik yaqiniga 45


# print(math.sin(90))  #sonning sin si

# print(math.factorial(5))  # 1*2*3*4*5

# print(math.log(144, 5))  #(5*5*5) == 5**3

# print(math.cos(180))


# son = int(input("Istalgan son k: "))
# print(math.sqrt(son))


# son = int(input("Istalgan son k: "))
# print(f"{son}ning factoriali {math.factorial(son)} ga teng")

# a = 8
# b = 2

# list -- ro'yxat
#   index         0       1      2           3         4|-2          5|-1
# qurulmalar = ["telfon", 'TV', 'wifi', 'sichqoncha', 'headphones', 'lamp']
# print(qurulmalar[0])
# print(qurulmalar[-1])


# # # ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# ismlar = ["ali", "olim", "vali"]

# # Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
# print(f"""Salom {ismlar[0].upper()}, 
# {ismlar[1].title()}, {ismlar[-1].title()} 
# ishlaring yaxshimi?""")

# malumot nomli list yasab f_name, year,
# address, phone larni list ichiga yozib qo'shing 
# va consolga listni chiqaring


# f_name = input("ism familya kiriting:  ")
# year = int(input("tug yil kiriting:  "))
# address = input("manzil:  ")
# phone = int(input("tel:  "))

# malumot = [f_name, year, address, phone]
# print(malumot)






# print(f"  ")   # f - string

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).

# sonlar = [22, -58.2, 34.0, 67, 1_983, 123_450_001, 112.4]
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

# friends = []
# print(friends)
# friends.append("John")
# friends.append("Alex")
# friends.append("Danny")
# friends.append("Sobirjon")
# friends.append("Vanya")
# print(f"To`liq list: {friends}")

# # Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
# friends.remove("John")
# friends.remove("Alex")
# del friends[-1]
# print(f"\nMehmonga Kelganlar-{friends}")


# talaba = ['jon', 'vaniya', 'kamol']
# print(talaba)
# talaba.append("Hasan") #oxiridan qosshish
# talaba.insert(0, "Husan")
# talaba.insert(2, "Ivan") #indexga qosshish

# print(talaba)
# print(len(talaba), "ta talaba") # uzunlik
# # uz - matn, py - string, en - text, ru - text



full_name = 'ali olimov'

print(len(full_name))




# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. 
# .pop() va .append() metodlari yordamida mehmonga kelgan 
# do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

# friends = []
# friends.append("John") # -
# friends.append("Alex") # -
# friends.append("Danny") # -
# friends.append("Sobirjon")
# friends.append("Vanya") # -

# mehmonlar = []
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(0))
# mehmonlar.insert(2, friends.pop(0))
# print("\nKelgan mehmonlar: ", mehmonlar)

# items = []
# print(items)
# items.append('phone')
# items.append('headphones')
# items.append('laptop')
# items.append('programs')
# items.append('games')
# items.append('limon')
# items.pop(-1)
# print(items)










    
    
    
    




