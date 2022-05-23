from uuid import uuid4

class Talaba:
    """Talaba nomli klass yaratamiz"""
    __num_class = 0
    
    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.__id = uuid4()
        Talaba.__num_class += 1
        
    @classmethod
    def get_num_class(cls):
        return cls.__num_class

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
        
# a_plus_b = list(map(lambda x, y: x + y, a, b))
# print(a_plus_b)
