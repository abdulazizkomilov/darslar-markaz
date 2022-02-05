<<<<<<< HEAD
# python_words = {
#     'integer':'Butun son',
#     'float': "O'nlik son",
#     'boolean':"Mantiqiy qiymat",
#     'for':"Biror amalni qayta-qayta bajarish tsikli",
#     'if':'Shartlarni tekshirish operatori'}

# for key, value in sorted(python_words.items()):
#     print(f"{key.title()} - {value}")
    

# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}

# print('Dunyo davlatlari:')
# for davlat in sorted(davlatlar):
#     print(davlat.upper())

# print('\nDavlatlarning poytaxtlari')
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())
    
    
# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
# capital = davlatlar.get(country)
# if capital==None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
    
    
# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }

# print('3 ta taom buyurtma bering.')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")




# # .items()
# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }

# print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# # .keys()
# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# print(mahsulotlar.keys())

# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())

# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")

# # LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# # .values()
# print(telefonlar.values())

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)


# # set

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'
#     }

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)

# # set
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)

=======
# python_words = {
#     'integer':'Butun son',
#     'float': "O'nlik son",
#     'boolean':"Mantiqiy qiymat",
#     'for':"Biror amalni qayta-qayta bajarish tsikli",
#     'if':'Shartlarni tekshirish operatori'}

# for key, value in sorted(python_words.items()):
#     print(f"{key.title()} - {value}")
    

# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}

# print('Dunyo davlatlari:')
# for davlat in sorted(davlatlar):
#     print(davlat.upper())

# print('\nDavlatlarning poytaxtlari')
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())
    
    
# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
# capital = davlatlar.get(country)
# if capital==None:
#     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
    
    
# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }

# print('3 ta taom buyurtma bering.')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")




# # .items()
# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }

# print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# # .keys()
# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# print(mahsulotlar.keys())

# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())

# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")

# # LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# # .values()
# print(telefonlar.values())

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)


# # set

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'
#     }

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)

# # set
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)

>>>>>>> 018ee822d02a0b90ace531a1e6855477cee54b21
# toys = {"ball","car","lamp","ball"}