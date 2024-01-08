class Avto:
    __num_avto = 0  #incapsulatsiya
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

    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.make} {self.model}. {self.narh}$"

    def __gt__(self, y):          # x > y
        return self.narh > y.narh
 
    def __lt__(self, y):          # x < y 
        return self.narh < y.narh
    
    def __le__(self, boshqa_avto):          # x <= y 
        return self.narh <= boshqa_avto.narh
    
    def __ge__(self, boshqa_avto):          # x >= y 
        return self.narh >= boshqa_avto.narh
    
    def __eq__(self, boshqa_avto):          # x == y 
        return self.narh == boshqa_avto.narh
    
    def __ne__(self, boshqa_avto):          # x != y 
        return self.narh !=  boshqa_avto.narh

    def get_info(self):
        return (
            f"{self.rang} {self.make} {self.model}.{self.yil}-yil. Narhi:{self.narh}$"
        )

avto = Avto("BMW", "x7", "qora", 2020, 40000)

# print(avto)  #__str__
# # str(avto)    #__str__
# # repr(avto)  #all str, print

avto1 = Avto("GM","Malibu","Qora",2020,60000)
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
#         return f"{self.name} avto saloni"

#     def __getitem__(self, index):    # salon1[2]  index kurish uchun
#         return self.avtolar[index]

#     def __setitem__(self, index, value):   # salon1[0] = Avto("Volva","K7","Oq",2017,50000)
#         if isinstance(value, Avto):
#             self.avtolar[index] = value

#     def add_avto(self, *qiymat):  # *args, # **kwargs == *key, *value
#         for avto in qiymat:
#             if isinstance(avto, Avto):
#                 self.avtolar.append(avto)
#             else:
#                 print("Avto obyketini kiriting")

# salon1 = AvtoSalon("MaxAvto")
# salon2 = AvtoSalon("Avto Lider")
# salon3 = AvtoSalon("Sam Avto")

# salon1.add_avto(avto1, avto2, avto3)
# salon2.add_avto(avto4, avto5, avto6)
# salon3.add_avto(avto)

# salon1[1] / salon3[5] / salon2[:]
# salon1[0] = Avto("Volva","K7","Oq",2017,50000)










# item 
# __num_items
# -- cls method ham necha martta ishlatilgani
# -- xususiyatlari: nomi, narh, yil, id
# -- method: __str__, __repr__, __gt__, __lt__,
     # __eq__, __nt__, __le__, __ge__





