# car = {"model": "ferrari", "rang": "qizil"}
# print(car["model"])
# print(car["rang"])

# lugat = {"salom": "hello", "kitob": "book"}
# print(f"salomning inglizcha tarjimasi - {lugat['salom']}")

# # Lug'atda istalgan ma'lumot turlarini saqlash mumkin
# talaba_0 = {  
#     'ism':'murod olimov',
#     'yosh': 22,
#     't_yil': 2000
# }
# print(f"""{talaba_0['ism'].title()}, 
# {talaba_0['t_yil']}-yilda tu'gilgan,
# {talaba_0['yosh']} yoshda""")

# # # Yangi kalit so'z va qiymat qo'shish
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# talaba_0['ism'] = 'abdulloh'
# # print(talaba_0)
# print(f"{talaba_0['ism'].title()}, \
#   {talaba_0['t_yil']}-yilda tu'gilgan,\
#   {talaba_0['yosh']} yoshda, \
#   {talaba_0['fakultet']} fakulteti,\
#   {talaba_0['kurs']} kursda")

# # Bo'sh lug'at
# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# # Qiymatni yangilash
# talaba_1['kurs'] = 4
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# # Kalit so'z-qiymat ni o'chirib tashlash
# talaba_0 = {
#     'ism':'murod olimov',
#     'yosh':22,
#     't_yil':2000
#     }
# print(talaba_0)
# del talaba_0['yosh']
# del talaba_0['t_yil']
# print(talaba_0)

# # Lu'gatlarni bir nechta qatorda yozish
# telefonlar = {
#     'ali':'iphone',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
# phone = telefonlar['ali']
# print(f"Alining telefoni {phone}")
# phone = telefonlar['vali']
# print(f"Valining telefoni {phone}")
# phone = telefonlar['hasan']
# print(f"Hasanning telefoni {phone}")

# # get() metodi
# phone = telefonlar.get('ali','Bunday ism mavjud emas')
# print(phone)

# phone = telefonlar.get('hasan', "hasan dick yuq")
# print(phone)

# sonlar = {}
# a_1 = int(input("a>>>  "))
# b_1 = int(input("b>>>  "))
# sonlar["a"] = a_1
# sonlar["b"] = b_1
# print(sonlar)


sonlar = {}
key = input("keyni kiriting>>>  ").lower()
value = input(f"{key}ga valueni kiriting>>>  ").lower()
sonlar[key] = value

print(sonlar)




