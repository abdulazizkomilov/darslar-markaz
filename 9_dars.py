# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     print('Sizga kirish bepul.')
# elif yosh <= 12:
#     print("Sizga kirish 5000 so'm")
# elif yosh <= 18:
#     print('Sizga kirish 8000 so`m')
# else:
#     print('Sizga kirish 10000 so\'m')


# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# else:
#     price = 10000
# print(f"Sizga kirish {price} so'm")



# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# else:
#     price = 8000

# print(f"Sizga kirish {price} so'm")


# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# elif yosh>=65:
#     price = 8000

# print(f"Sizga kirish {price} so'm")

# kun = input("Bugun nima kun?>>> ")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday? "))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")

# non = input("""Buyurtmachi non oldimi? 
# Olgan bulsa '1' deb yozing
# >>> """)

# choy = True  #yes 1 | no 0
# salat = False
# price = 15000
# if choy and salat:
#     price = price + 10000
# elif choy or salat:
#     price = price + 5000

# print(f"Jami {price} so'm")

# narh = 15000 # mijoz 15 so'mga ovqat oldi
# choy = True  #  1
# salat = False   # 0
# non = True
# kompot = True
# assorti = False

# if choy:
#     print("Mijoz choy oldi.")
#     narh += 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000

# print(f"Jami {narh} so'm")

# ism = input("Ta`laba ism va familyasini kiriting: ")
# baho = int(input(f"{ism.capitalize()}ni baholang>>> "))
# if baho == 5:
#     print("A`lo")
# elif baho == 4:
#     print("Yaxshi")
# elif baho <= 3:
#     print("Yomon")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>> ')
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print('Buyurtma qabul qilindi.')

# menu = []
# for son in range(1, 6):
#     menu.append(input(f"{son}-ta`omni kiriting: "))
# taom = input("Nima táom buyyrtma qilasiz: ")
# if taom not in menu:
#     print(f"Kechirasiz bizda {taom} yuq! Bizdagi táomlar róyxati: ")
#     for a in menu:
#         print(a, end=("\n"))
#     taom_2 = input("Iltimos quydagi táomlardan buyurtma qiling: ")
#     print(f"{taom_2} qabul qilindi!")
# else:
#     print(f"{taom} qabul qilindi!")    
 
# menu ga kamida 5ta táom qóshisin...


# for a in menu:
#     print(a, end=("\n"))



# yil2 = input("Yoshingiz nechida? ")

# yosh = '18'
# print(yosh.isdigit())

# yil = "7"
# print(yil.isdigit())

# yil2 = "2"
# print(yil2.isalnum())

# yosh = input("Yoshingiz nechida? ")
# if yosh.isdigit():
#     yosh = float(yosh)
# else:
#     print("Matnli raqam ")


# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else:
#     print("Savatchangiz bo'sh!")