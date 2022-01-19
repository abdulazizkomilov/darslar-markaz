class Avto:
    __num_avto = 0
    """Avtomobil klassi"""

    def __init__(self, make, model, rang, yil, narh, km=1000):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        Avto.__num_avto += 1

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    
    def get_km(self):
        return self.__km

    def __str__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.make} {self.model}. {self.narh}$"

    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.make} {self.model}. {self.narh}$"

    def __eq__(self, boshqa_avto):
        return self.narh == boshqa_avto.narh

    def __lt__(self, boshqa_avto):
        return self.narh < boshqa_avto.narh
    
    def __le__(self, boshqa_avto):
        return self.narh <= boshqa_avto.narh

    def get_info(self):
        return (
            f"{self.rang} {self.make} {self.model}.{self.yil}-yil. Narhi:{self.narh}$"
        )

# avto11 = Avto("BMW", "x7", "qora", "2020", 60000)
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
avto6 = Avto("Honda","Accord","Oq",2017,42000)

# class AvtoSalon:
#     """Avtosalon klassi"""

#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosaloni"

#     def __len__(self):
#         return len(self.avtolar)

#     def __getitem__(self, index):
#         return self.avtolar[index]

#     def __setitem__(self, index, value):
#         if isinstance(value, Avto):
#             self.avtolar[index] = value

#     def __add__(self, qiymat):
#         if isinstance(qiymat, AvtoSalon):
#             yangi_salon = AvtoSalon(f"{self.name} {qiymat.name}")
#             yangi_salon.avtolar = self.avtolar + qiymat.avtolar
#             return yangi_salon
#         elif isinstance(qiymat, Avto):
#             self.add_avto(qiymat)
#         else:
#             print(f"AvtoSalon ga {type(qiymat)} qo`shib bo`lmaydi")

#     def __call__(self, *param):
#         if param:
#             for avto in param:
#                 self.add_avto(avto)
#         else:
#             return [avto for avto in self.avtolar]

#     def add_avto(self, *qiymat):
#         for avto in qiymat:
#             if isinstance(avto, Avto):
#                 self.avtolar.append(avto)
#             else:
#                 print("Avto obyketini kiriting")

#     def get_list(self):
#         return [avto for avto in self.avtolar]

# # salon3 = AvtoSalon("Sam Avto")
# salon1 = AvtoSalon("MaxAvto")
# salon2 = AvtoSalon("Avto Lider")

# salon1.add_avto(avto1, avto2, avto3)
# salon2.add_avto(avto4, avto5, avto6)

# newAvto = Avto("BMW", 'X7','Qora',2015,75000)
# salon1 + newAvto
# print(salon1[:])

# # salon1 = AvtoSalon("MaxAvto")
# # avto_new = Avto("Mercedes-Benz", 'E200','Silver',2015,80000)

# # # Obyektni chaqiramiz:
# # salon1(avto_new) # Yangi avto qo'shamiz
# # salon1() # salondagi mashinalarni ko'ramiz


# # AMALIYOT
# # Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metodlarni qo'shishni mashq qiling.
# # Obyekt haqida ma'lumot (__rerp__)
# # Talabalarni bosqichi bo'yicha solishtirish (__lt__, __eg__ va hokazo)
# # Fan degan yangi klass yarating. Fan obyetklari tarkibida shu fanga yozilgan talabalarning ro'yxati saqlansin. Buning uchun Fanga add_student(), __getitem__, __setitem__, __len__ kabi metodlarni qo'shing.
# # Fanga qo'shish + operatori yordamida talaba qo'shish metodini yozing
# # Minus (-) operatori yordamida fandan talaba olib tashlash metodini yozing (bunda talabaning passport raqami yoki ID raqami bo'yicha topib, olib tashlash mumkin)
# # Fan obyektlarini chaqiriladigan qiling (masalan, fizika(), yoki fizika(talaba1)). Bu metodlarni o'zingiz istagandek talqin qiling.