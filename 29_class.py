# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya} {self.tyil} da tug`ulgan. {self.bosqich}-bosqich talabasi "
    
#     def set_bosqich(self,bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
        
#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1
        
# talaba1 = Talaba("Alijon","Valiyev",2000)
# # print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# # print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# # print(talaba1.get_info())


# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
        
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]
        
        
# # # ma'lomotlar 
# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba2 = Talaba("Hasan","Alimov",2001)
# talaba3 = Talaba("Akrom","Boriyev",2001)

# talaba1.update_bosqich()
# talaba2.update_bosqich()
# talaba3.update_bosqich()

# # # # talaba qo`shamiz
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# # print(matematika.talabalar_soni)
# # print(matematika.talabalar)

# mat_talabalar = matematika.get_students()
# # print(mat_talabalar)


class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
      
    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich
        
    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1    
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
    
    def get_age(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil-self.tyil
    
    
# class Fan():
#     """Fan nomli klass"""
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
    
#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi
    
#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumot"""
#         return [x.get_info() for x in self.talabalar]
    
#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni
    
# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba2 = Talaba("Hasan","Alimov",2001)
# talaba3 = Talaba("Akrom","Boriyev",2001)

# dir()    
dir(Talaba)

# # Dunder — double underscore (ikki pastki chiziq) so'zlarining qisqartmasi.

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Talaba))


# print(see_methods(talaba1))

# print(talaba1.__dict__)

# print(talaba1.__dict__.keys())


# AMALIYOT
# Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)
# Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
# get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
# Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
# update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
# Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
# Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
# Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
# Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
# dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)