class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
    
    def get_info(self):
        return f"""{self.ism} {self.familiya} 
{self.tyil} da tug`ulgan. 
{self.bosqich}-bosqich talabasi"""
    
    def set_bosqich(self, qiymat):
        self.bosqich = qiymat
        
    def update_bosqich(self):
        self.bosqich += 1
# talaba1 = Talaba("Alijon", "Valiyev", 2000)

# talaba_2 = Talaba("Abror", "Muminboyev", 2010)

# print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())


class Fan:
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
    
    def add_student(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
    
    def get_name(self):
        return self.nomi
    
    def get_students(self):
        return [x.get_info() for x in self.talabalar]
      
    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni
 
matematika = Fan("Oliy Matematika")
english = Fan("English")

# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba2 = Talaba("Hasan","Alimov",2001)
# talaba3 = Talaba("Akrom","Boriyev",2001)

# # # talaba qo`shamiz
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(matematika.talabalar_soni)
# print(matematika.get_students())

# # return [x.get_info() for x in self.talabalar]
# mat_talabalar = matematika.get_students()
# print(mat_talabalar)

# # # dir()    
# dir(Talaba)

# Dunder — double underscore (ikki pastki chiziq) so'zlarining qisqartmasi.

# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]
    
    # for method in dir(klass):
    #     if method.startswith('__') is False:
    #         return method

# print(see_methods(Talaba))
# print(see_methods(talaba1))
# print(see_methods(matematika))


# print(talaba1.__dict__)

# print(talaba1.__dict__.keys())
# print(talaba1.__dict__.values())

class Sinf:
    def __init__(self, nomi, kurs, raxbar, xona):
        self.nomi = nomi
        self.kurs = kurs
        self.talabalar = []
        self.talabalar_soni = 0
        self.raxbar = raxbar
        self.xona = xona
        self.fanlar = []
        
    def add_student(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
    
    def get_name(self):
        return self.nomi
    
    def get_students(self):
        return [x.get_info() for x in self.talabalar]
      
    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni
    
        

talaba1 = Talaba("Aziz","Valiyev",2000)
talaba2 = Talaba("Isfandiyor","Alimov",2001)
talaba3 = Talaba("Jamshid","Boriyev",2001)
        
sinf_10_i = Sinf('I', 10, 'KKK', 12)

sinf_10_i.add_student(talaba1)
sinf_10_i.add_student(talaba2)
sinf_10_i.add_student(talaba3)













