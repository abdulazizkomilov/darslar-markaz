# from uuid import uuid4

# # class Avto:
# #     """Avtomobil klassi"""

# #     def __init__(self, make, model, rang, fan, yil, narh, km=0):
# #         """Avtomobilning xususiyatlari"""
# #         self.make = make
# #         self.model = model
# #         self.rang = rang
# #         self.fan = fan
# #         self.yil = yil
# #         self.narh = narh
# #         self.__km = km
# #         self.__id = uuid4()
    

# #     def get_km(self):
# #         return self.__km

# #     def get_id(self):
# #         return self.__id

# #     def add_km(self, km):
# #         """Mashinaning km ga yana km qo'shish"""
# #         if km >= 0:
# #             self.__km += km
# #         else:
# #             print("Mashina km kamaytirib bo'lmaydi")


# # avto1 = Avto("GM","Malibu","Qora", "matematika",2020,40000,1000)
# # print(f"ID: {avto1.get_id()}")
# # avto1.add_km(1500)
# # print(avto1.get_km())


# class Avto:
#     """Avtomobil klassi"""

#     __num_avto = 0

#     def __init__(self, make, model, rang, yil, narh, km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1

#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto

#     def get_km(self):
#         return self.__km

#     def get_id(self):
#         return self.__id

#     def add_km(self, km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km >= 0:
#             self.__km += km
#         else:
#             print("Mashina km kamaytirib bo'lmaydi")

# avto1 = Avto("GM","Malibu","Qora",2020,40000,1000)
# avto2 = Avto("GM","Malibu","matematika",2020,40000,1000)
# avto3 = Avto("GM","Malibu","Qora",2020,40000,1000)
# avto4 = Avto("GM","Malibu","matematika",2020,40000,1000)
# # class Bus:
# #     pass


# # class Train:
# #     pass


# # AMALIYOT
# # Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar qo'shing va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
# # Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.
# # Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing