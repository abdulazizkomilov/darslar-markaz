# # VORISLIK VA POLIMORFIZM

# class Shaxs:
#     """Shaxslar haqida ma'lumot"""

#     def __init__(self, ism, familiya, passport, tyil):
#         """Shaxsning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil

#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info

#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil

# shaxs1 = Shaxs("Murod", "Habibullayev", "FA1980923", 2004)

# class Manzil:
#     """Manzil saqlash uchun klass"""

#     def __init__(self, uy, kocha, tuman, viloyat):
#         """Manzil xususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat

#     def get_manzil(self):
#         """Manzilni ko'rish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
#         return manzil


# talaba1_manzil = Manzil(12, "Olmazor", "Bog'bon", "Samarqand")

# class Talaba(Shaxs):
#     """Talaba klassi"""

#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil

#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam

#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich

#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}, {talaba1_manzil.get_manzil()}."
#         return info

# # talaba1 = Talaba("Murod", "Habibullayev", "AB8758765", 2004, "N9891001", "Yangiyer")



# talaba1 = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012", talaba1_manzil)



# # AMALIYOT
# # Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
# # Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
# # Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
# # Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.
# # Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)
# # Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
# # Barcha yangi klasslar uchun get_info() metodini qayta yozib chiqing.
# # Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan Admin klassini yarating.
# # Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" degan matn chiqarsin.