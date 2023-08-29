"""
OOP (Object Oriented Programming)

- Encapsulation
- Polimorfizm
- Inheritance
- Abstraction
"""

# #       --- __init__  initialization (ishga tushirish) ---

# class Process:
#     def __init__(self):
#         print("Jarayon ishga tushdi.")
        
# Process()


# # method va xususiyatlar

#                      Mashina
# 
#        xususiyatlari                   methodlari
#       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓               ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   
#   |     kampaniyasi        |           info()         |
#   |     modeli             |           price()        |
#   |     rangi              |           get_km()       |
#   |     yili               |           set_km()       |
#      


# class Car:
#     """" Mashina uchun Car nomli class """
#     def __init__(self, company, model, color, year, price=None, km=0):
#         self.company = company
#         self.model   = model
#         self.color   = color
#         self.year    = year
#         self.price   = price
#         self.km      = km
        
#     def __repr__(self):
#         return f"Ushbu mashinaning kampaniyasi: {self.company}, modeli: {self.model},\
# rangi: {self.color}, ishlab chiqarilgan yili: {self.year}"
        
#     def info(self):
#         """" Mashina haqida to`liq ma`lumot qaytaruvchi funksiya"""
#         return f"Ushbu mashinaning kampaniyasi: {self.company}, modeli: {self.model},\
# rangi: {self.color}, ishlab chiqarilgan yili: {self.year}"
    
#     def get_price(self):
#         """" Mashinaning narxi haqida ma`lumot qaytaruvchi funksiya"""
#         if self.price:
#             narx = f'{self.model}ning narxi {self.price}$'
#         else:
#             narx = f'{self.model}ning narxi hozircha ommaga taqdim etilmagan.'
#         return narx

#     def get_km(self):
#         """" Mashinaning yurgan km haqida ma`lumot qaytaruvchi funksiya"""
#         if self.km >= 0:
#             km = f'{self.model} {self.km}km yurgan km'
#         else:
#             km = f'{self.model} hali yangi yurmagan.'
#         return km
    
#     def set_km(self, km):
#         """" Mashinaga km qo`shib boradigan funksiya"""
#         if km > 0:
#             self.km += km
#         else:
#             return "funksiya to`g`ri maqsadda ishlatilmayabdi."
        
# c1 = Car("Tesla", "Modul Y", "qizil", "2022")
# c2 = Car("Tesla", "Modul X", "oq", "2022", 50_000, 10_000)



# #       ---  Encapsulation  --- 

# class Person:
#     """ Encapsulation """
    
#     __count = 0
    
#     def __init__(self, ism, familya, id_num):
#         self.ism       = ism
#         self.familya   = familya
#         self.__id_num  = id_num
#         Person.__count += 1
        
#     @classmethod
#     def counter(cls):
#         return cls.__count
        
#     def __repr__(self):
#         return f'{self.ism.title()} haqida ma`lumotlar to`plami.'
    
#     def get_id_num(self):
#         return f'{self.ism.title()}ning id raqami {self.__id_num}.'
        
    
# p1 = Person('olim', "hakimov", "AD1234567")
# p2 = Person('umar', "husanov", "AD0987654")

    

#       ---  Inheritance  --- 

from uuid import uuid4

class Talaba:
    def __init__(self, talaba_name, familya):
        self.talaba_name           = talaba_name
        self.familya  = familya
        self.student_id   = uuid4()
        
    def get_name(self):
        return f"Ta`laba {self.talaba_name} {self.familya}"

class Group:
    def __init__(self, name, duration_group):
        self.name           = name
        self.num_students   = 0
        self.uuid           = uuid4()
        self.students       = []
        self.duration_group = duration_group
        
    def __repr__(self):
        return f"{self.name} guruhi, ID: {self.uuid}."
    
    def get_num_students(self):
        return f'{self.name} guruhida {self.num_students} ta`laba mavjud.'
    
    def get_duration(self):
        return f'Davomiyligi {self.duration_group} oy.'
    
    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        pass
    
class Math(Group):
    def __init__(self, name, duration_group, teacher, talaba):
        super().__init__(name, duration_group)
        self.teacher  = teacher
        
    def about(self):
        return f"{self.name} guruhi, ID: {self.uuid}, o`qituvchi: {self.teacher}"
    
    def add_students(self, student):
        self.students.append(student)
        self.num_students += 1
        
    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return self.students
        
t1 = Talaba("olin", "kamolov")

m1 = Math("Algebra", 8, "Umarov Aktam")
m1.add_students('Ilhom')
m1.add_students('Kamol')
m1.add_students('G`olib')    

# m2 = Math("Basic Geometry", 4, "Azimov Rustam")
# m2.add_students('Yusuf')
# m2.add_students('Eldor')
# m2.add_students('Husan')   
# m2.add_students('Hasan')    



# #       ---  Polimorfizm  --- 

# class Transport:
#     def __init__(self, name=''):
#         self.name = name
#     def move(self):
#         return 'it`s moving'
   
# class Car(Transport):
#     def move(self):
#         print(f"{self.name} moves very quickly!")
       
# class Plane(Transport):
#     def move(self):
#         print(f"{self.name} flew very high!")

# class Train(Transport):
#     def move(self):
#         print(f"{self.name} drives on average!")
       
# a = Transport()
# a.move()
# c = Car("Tesla")
# c.move()
# d = Plane("F12")
# d.move()
# d = Train("Freight trains")
# d.move()


# #       ---  Abstraction  --- 

# from abc import ABCMeta, abstractmethod, abstractstaticmethod

# class Department(metaclass=ABCMeta):
    
#     @abstractmethod 
#     def __init__(self, employees):
#         """implement in child class """
        
#     @abstractstaticmethod 
#     def print_department():
#         """implement in child class """
        
        
# class Accounting(Department):
#     def __init__(self, employees):
#         self.employees = employees
    
#     def print_department(self):
#         print(f"Accounting Department: {self.employees}")
        

# class Development(Department):
#     def __init__(self, employees):
#         self.employees = employees
    
#     def print_department(self):
#         print(f"Development Department: {self.employees}")
        
    

# class ParentDepartment(Department):
#     def __init__(self, employees):
#         self. employees     = employees
#         self.base_employees = employees
#         self.sub_depts      = []
        
#     def add(self, dept):
#         self.sub_depts.append(dept)
#         self.employees += dept.employees
    
#     def print_department(self):
#         print("Parent Department")
#         print(f"Parent Department Base Employees: {self.base_employees}")
#         for dept in self.sub_depts:
#             dept.print_department()
#             print(f"Total number of employees: {self.employees}")
    
# dept1 = Accounting(170)
# dept2 = Development(230)

# parent_dept = ParentDepartment(30)
# parent_dept.add(dept1)
# parent_dept.add(dept2)
        
        
        
        
        
        
        


    

