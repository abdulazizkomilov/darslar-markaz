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
#               {self.tel}""")


# talaba1 = Talaba("Alijon", "Valiyev", 2000, 99893208399)
# talaba2 = Talaba("Hasan", "Umarov", 1995, 9983737593)

# print(talaba1.ism)
# print(talaba1.familiya)
# talaba2.tanishtir()

# talaba2 = Talaba("Olim","Hakimov", 2001, 901234567)
# talaba2.tanishtir()
# talaba3 = Talaba("Husan", "Akbarov", 2004, 234567890)
# talaba4 = Talaba("Hasan", "Akbarov", 2004, 987654453)
# talaba4.tanishtir()



# class Talaba:
#     """Talaba nomli klass yaratamiz"""

#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism

#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya

#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"

#     def get_age(self, yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil - self.tyil

#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya} {self.tyil} yilda tu'gilganman")


# talaba1 = Talaba("olim", "Hakimov", 2005)
# print(talaba1.get_fullname())
# print(talaba1.get_age(2022))

# talaba1.tanishtir()

class Talaba1():
    
    def __init__(self, ism, familya, tyil):
        self.ism = ism
    
    def get_name(self):
        pass
    
    def get_lastname(self):
        pass
    
    def get_fullname(self):
        pass
    
    def get_age(self):
        pass
    
    def tanishtir(self):
        pass

