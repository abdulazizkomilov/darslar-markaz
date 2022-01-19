# class Talaba:
#     """Talaba nomli klass yaratamiz"""

#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya} {self.tyil} yilda tu'gilganman")


# talaba1 = Talaba("Alijon", "Valiyev", 2000)
# talaba2 = Talaba("Hasan", "Umarov", 1995)

# print(talaba1.ism)
# print(talaba1.familiya)
# talaba2.tanishtir()

# talaba2 = Talaba("Olim", "Olimov", 1995)
# talaba2.tanishtir()
# talaba3 = Talaba("Husan", "Akbarov", 2004)
# talaba4 = Talaba("Hasan", "Akbarov", 2004)
# talaba4.tanishtir()



class Talaba:
    """Talaba nomli klass yaratamiz"""

    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def get_age(self, yil):
        """Talabaning yoshini qaytaradi"""
        return yil - self.tyil

    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya} {self.tyil} yilda tu'gilganman")


talaba1 = Talaba("Alijon", "Valiyev", 2000)
print(talaba1.get_fullname())
print(talaba1.get_age(2021))

talaba1.tanishtir()

# class Talaba1():
#     # /sknda.fkn
#     def __init__(self, ism, familya, tyil):
#         self.ism = ism
    
    
#     def get_name(self):
#         pass
    
#     def get_lastname(self):
#         pass
    
#     def get_fullname(self):
#         pass
    
#     def get_age(self):
#         pass
    
#     def tanishtir(self):
#         pass

