"""
VORISLIK VA POLIMORFIZM 

Vorislik (Encapsulation) va polimorfizm, obyektiv dasturlash 
(object-oriented programming) ning asosiy 
tamoyillari hisoblanadi.

1. Vorislik (Encapsulation):
    
   - Vorislik, ma'lumotlarni va funksiyalarni 
   bir obyekt ichida yig'ib olish va ularga 
   chegaralanish prinsipi.
   
   - Obyektning ichki xususiyatlarini va metodlarini 
   tashkil etishda ishlatiladi.
   
   - Boshqa obyektga mo'ljallangan ma'lumotlarga 
   to'xtash va ularga faqat obyektning o'zidan 
   murojaat qilish mumkin.
   
   - Sirtqi interfeysni o'z ichiga olgan sinflar, 
   vorislik prinsipini amalga oshiradilar.


2. Polimorfizm:
    
   - Polimorfizm, bir obyektni o'z metodlari 
   orqali boshqarish imkoniyatini ta'minlaydigan prinsip.
   
   - Bir sinf ichidagi bir metod, har xil 
   turlardagi obyektga qo'llanilishi mumkin.
   
   - Polimorfizm, metodlarning bir biri orasida 
   ayirboshlash imkoniyatini ta'minlayadi.
   
   - Polimorfizm, qo'llanish turlarini chaqirishda 
   yagona interfeys orqali, obyekt turlarini 
   farq etmaslikni o'zaro murojaat etishni ta'minlaydi.

"""

# class Shaxs:
#     """Shaxslar haqida ma'lumot"""

#     def __init__(self, ism, familiya, passport, tyil):
#         """Shaxsning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil

#     def get_info(self):
#         """Shaxs haqida ma'lumot"
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info

#     def get_age(self, yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil
    
    
# # VORISLIK ota klassdan meros
# class Talaba(Shaxs):
#     """Talaba klassi"""

#     def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
#         """Talabaning xususiyatlari"""
#         # Ota klasslarning __init__ metodlarini chaqirish plomarfizm
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
#         info = f"{self.ism} {self.familiya}. Manzil: {self.manzil} "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info

# talaba1 = Talaba("olim", "karimov", "AB3457261", 1997, "ID56782", "yangiyer")
# shaxs1 = Shaxs("olim", "karimov", "AB3457261", 1997)
# shaxs2 = Shaxs("vali", "kamolov", "BC7922639", 1980)





class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Ismi: {self.name}, Yosh: {self.age}")


class Occupation:
    def __init__(self, occupation):
        self.occupation = occupation

    def display_occupation(self):
        print(f"Kasbi: {self.occupation}")


class Student(Person, Occupation):
    def __init__(self, name, age, student_id, occupation):
        # Ota klasslarning __init__ metodlarini chaqirish
        Person.__init__(self, name, age)
        Occupation.__init__(self, occupation)
        self.student_id = student_id

    def display_info(self):
        # Ota klasslarning display_info metodlarini chaqirish
        Person.display_info(self)
        # Bu sinfning xususiy metodini qo'shish
        print(f"Talaba ID: {self.student_id}")

# Test qismi
student = Student("Alice Smith", 20, "S12345", "IT Specialist")
student.display_info()
student.display_occupation()



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
