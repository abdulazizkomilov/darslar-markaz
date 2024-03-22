"""
OOP, yoki Ob'ektga yo'naltirilgan 
dasturlash, dasturlashning bir 
usuli bo'lib, dasturchilarga ob'ektlarni
yaratish, ularga kerakli xususiyatlar 
va metodlarni berish, shuningdek 
ulardan foydalanishni o'rgatadi. 
Bu, kodni tuzatish va boshqa dasturlash 
prinsiplari bilan solishtirishni 
osonlashtiradi.
"""

"""
Xususiyat    -----  malumotlari
Metod        -----  funksiya
"""

# class Xodim:
#     def __init__(self, ism, familiya, yosh):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh
    
#     def tanishtir(self):
#         return f"Xodimning ismi: {self.ism.title()}, familiyasi: {self.familiya.title()}, yoshi: {self.yosh}"
        
#     def t_yil(self):
#         return f"Xodimning tugulgan yili: {2024 - self.yosh}"

# xodim1 = Xodim("temur", "nosirov", 13)





# class Telefon:
#     def __init__(self, model, narx):
#         self.model = model
#         self.narx = narx
#         self.xotira = 64
        
#     def __repr__(self):
#         return f"Telfon: {self.model}, {self.narx}$"
        
#     def xotira_qolganini_korsat(self):
#         return f"{self.model} telefonida {self.xotira} GB xotira qolgan." 
 
#     def narxni_ozgartir(self, yangi_narx):
#         self.narx = yangi_narx

# telefon1 = Telefon("iPhone", 1200)
# telefon2 = Telefon("Samsung1", 800)



# print(f"{telefon1.model}: {telefon1.narx}")

# telefon1.xotira_qolganini_korsat()
# telefon2.xotira_qolganini_korsat()

# telefon1.narxni_ozgartir(1300)
# print(f"{telefon1.model} telefonining yangi narxi: {telefon1.narx} dollarni tashkil etadi.")




# class Talaba:
#     """Talaba nomli klass yaratamiz"""

#     def __init__(self, ism, familiya, tyil, tel):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.tel = tel

#     def get_f_name(self):
#         return f"To`liq ism familiyam: {self.ism} {self.familiya}"
    
#     def get_tel(self):
#         return self.tel


#     def tanishtir(self):
#         print(f"""Ismim {self.ism} {self.familiya} {self.tyil} yilda tu'gilganman, 
# {self.tel}""")


# talaba1 = Talaba("Alijon", "Valiyev", 2000, 99893208399)
# talaba2 = Talaba("Hasan", "Umarov", 1995, 9983737593)
# talaba3 = Talaba("Zarnigor", "Juraboyiva", 2006, 42342342)
# talaba4 = Talaba("Samandar", "Hazratqulov", 2008, 906862808)
# talaba5 = Talaba("Sanjar", "Ismoilov", 2008, 932575708)



# print(talaba1.ism)
# print(talaba1.familiya)
# talaba1.tanishtir()






# class Talaba:
#     """Talaba nomli klass yaratamiz"""

#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

    # def get_name(self):
    #     """Talabaning ismini qaytaradi"""
    #     return self.ism

    # def get_lastname(self):
    #     """Talabaning familiyasini qaytaradi"""
    #     return self.familiya

    # def get_fullname(self):
    #     """Talabaning ism-familiyasini qaytaradi"""
    #     return f"{self.ism} {self.familiya}"

    # def get_age(self, yil):
    #     """Talabaning yoshini qaytaradi"""
    #     return yil - self.tyil

    # def tanishtir(self):
    #     print(f"Ismim {self.ism} {self.familiya} {self.tyil} yilda tu'gilganman")

# talaba1 = Talaba("olim", "Hakimov", 2005)
# print(talaba1.get_fullname())
# print(talaba1.get_age(2023))
# talaba1.tanishtir()


class Shaxs:
    
    def __init__(self, ism, familya, tyil):
        pass
    
    def get_name(self):
        pass
    
    def get_age(self):
        pass
    
    def tanishtir(self):
        pass

