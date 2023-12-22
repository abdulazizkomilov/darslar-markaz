# 1:
#     Javob: 
#     ```python
#     def yigindi_tekshirish():
#         son1 = int(input("Birinchi sonni kiriting: "))
#         son2 = int(input("Ikkinchi sonni kiriting: "))
        
#         yigindi = son1 + son2
        
#         if yigindi > 10:
#             print("Katta!")
#         else:
#             print("Kichik!")

#     yigindi_tekshirish()
#     ```
    
    
# 2:
#     Javob:
#     ```python
#     for i in range(1, 11, 2):
#         print(i)
#     ```
    
# 3:
#     Javob:
#     ```python
#     soz = input("Soz kiriting: ")
    
#     index = 0
#     while index < len(soz):
#         print(soz[index])
#         index += 1
#     ```
    
    
# 4:
#     Javob:
#     ```python
#     class Shaxs:
#         def __init__(self, ism, yosh, kasb):
#             self.ism = ism
#             self.yosh = yosh
#             self.kasb = kasb

#         def taniqli_malumot(self):
#             print(f"{self.ism} {self.yosh} yoshda, kasbi: {self.kasb}")

#     shaxs1 = Shaxs("Ali", 25, "Dasturchi")
#     shaxs1.taniqli_malumot()
#     ```
    
    
# 5:
#     Javob:
#     ```python
#     class Talaba(Shaxs):
#         def __init__(self, ism, yosh, kasb, kurs):
#             super().__init__(ism, yosh, kasb)
#             self.kurs = kurs

#     talaba1 = Talaba("Vali", 20, "Dasturchi", 3)
#     print(f"{talaba1.ism} {talaba1.yosh} yoshda, kasbi: {talaba1.kasb}, {talaba1.kurs}-kurs talabasi")
#     ```
    
    
# 6:
#     Javob:
#     ```python
#     class Cart:
#         def __init__(self):
#             self.mahsulotlar = []

#         def mahsulot_qo'shish(self, mahsulot):
#             self.mahsulotlar.append(mahsulot)

#         def mahsulot_olib_tashlash(self, mahsulot):
#             self.mahsulotlar.remove(mahsulot)

#         def umumiy_narx(self):
#             return sum([mahsulot.narx for mahsulot in self.mahsulotlar])

#     class Mahsulot:
#         def __init__(self, nom, narx):
#             self.nom = nom
#             self.narx = narx

#     # Foydalanish
#     cart = Cart()
#     mahsulot1 = Mahsulot("Telefon", 1500)
#     mahsulot2 = Mahsulot("Kompyuter", 2500)

#     cart.mahsulot_qo'shish(mahsulot1)
#     cart.mahsulot_qo'shish(mahsulot2)
#     print("Umumiy narx:", cart.umumiy_narx())
#     ```
    
    
# 7:
#     Javob:
#     ```python
#     class User:
#         def __init__(self, ism):
#             self.ism = ism
#             self.savat = Cart()

#         def savatga_mahsulot_qo'shish(self, mahsulot):
#             self.savat.mahsulot_qo'shish(mahsulot)

#         def savatdan_mahsulot_olib_tashlash(self, mahsulot):
#             self.savat.mahsulot_olib_tashlash(mahsulot)

#         def umumiy_xarajat(self):
#             return self.savat.umumiy_narx()

#     # Foydalanish
#     foydalanuvchi = User("John")
#     foydalanuvchi.savatga_mahsulot_qo'shish(mahsulot1)
#     foydalanuvchi.savatga_mahsulot_qo'shish(mahsulot2)
#     print(f"{foydalanuvchi.ism}ning savati umumiy {foydalanuvchi.umumiy_xarajat()} so'm")
#     ```
    
    








