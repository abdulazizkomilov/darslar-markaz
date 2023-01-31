# def talabani_bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = int(baho)
#     return baholar



# baho = talabani_bahola(["ali", "vali", "hasan", "husan"])
# print(baho)





# talabalar = ["ali", "vali", "hasan", "husan"]

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = baho
#     return baholar


# baholar = bahola(talabalar[:])
# print(baholar)
# print(talabalar)



# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))









# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)


# print(summa(1, 2, 3, 4, 5))
# print(summa(1, 2, 3, 9, 10))


# def summa(x, y, *sonlar):    #args
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x + y + sum(sonlar)


# print(summa(5, 4))
# print(summa(1, 2, 3, 4, 5, 8, 13, 18))
# print(summa(9, 11))

# def avto_info(kompaniya, model, **malumotlar): #kwargs
#     """Avto haqidagi ma'lumotlarni 
#     lug'at ko'rinishdia 
#     qaytaruvchi funksiya"""
#     malumotlar["kompaniya"] = kompaniya
#     malumotlar["model"] = model
#     return malumotlar


# avto1 = avto_info("GM", "malibu", rang="qora", yil=2018)
# avto2 = avto_info("Kia", "K5", rang="qizil", narh=35000, yil=2020, korobka="avtomat")
# avto3 = avto_info('BMW', 'S50')



sonlar = [1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 10,
 11,
 12,
 13,
 14,
 15,
 16,
 17,
 18,
 19,
 20,
 21,
 22,
 23,
 24,
 25,
 26,
 27,
 28,
 29,
 30,
 32,
 33,
 34,
 35,
 36,
 37,
 38,
 39,
 40,
 41,
 42,
 43,
 44,
 45,
 46,
 47,
 48,
 49,
 50,
 51,
 52,
 53,
 54,
 55,
 56,
 57,
 58,
 59,
 60,
 61,
 62,
 63,
 64,
 65,
 66,
 67,
 68,
 69,
 70,
 71,
 72,
 73,
 74,
 75,
 76,
 77,
 78,
 79,
 80,
 81,
 82,
 83,
 84,
 85,
 86,
 87,
 88,
 89,
 90,
 91,
 92,
 93,
 94,
 95,
 96,
 97,
 98,
 99,
 100]










