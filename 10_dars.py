# def toliq_ism_yasa(ism, familiya): # args - parms
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism

# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "olimov")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# print(f"{talaba1} darsga kechikib keldi")


# def toliq_ism_yasa(ism, familiya, otasining_ismi=""):
#     """Toliq ism va familiya qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa("ali", "jamolov")
# talaba2 = toliq_ism_yasa("hakim", "olimov", "abrorovich")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")




# def friends_list():
#     """friends list"""
#     print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
#     ismlar = []
#     n = 1  # ismlarni sanash uchun o'zgaruvchi
#     while True:  # loop
#         savol = f"{n}-do'stingiz ismini kiriting: "
#         ism = input(savol)
#         ismlar.append(ism)
#         takrorlash = input("ism qo'shasizmi? (ha/yo'q)")
#         n += 1
#         if takrorlash != "ha":
#             break     
#     print("Do'stlaringiz ro'yxati: ")
#     for ism in ismlar:
#         print(ism.title(), end=" ")
        
# friends_list()
        
# while --- cheksiz davom etadi loop 
# break --- for yoki while ni to'xtatadi    
# for   --- loop yoki tsikl    
# def   --- funksiya yasash uchun ishlatiladi



# def friends_list_data():
#     """friends list data"""    
#     print("Do'stlaringiz yoshini saqlaymiz.")
#     dostlar = {}
#     ishora = True
#     n = 1
#     while ishora:
#         ism = input(f"{n} - do'stingiz ismini kiriting: ")
#         yosh = int(input(f"{ism.title()}ning yoshini kiriting: "))
#         dostlar[ism] = yosh
#         n+=1
#         javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#         if javob != "ha":
#             ishora = False
#     for ism, yosh in dostlar.items():
#         print(f"{ism.title()} {yosh} yoshda")

    
    
    
# def set_ball():
#     """set ball users"""
#     talabalar = ["hasan", "husan", "olim", "botir"]
#     baholangan_talabalar = {}
#     while talabalar:
#         talaba = talabalar.pop()
#         baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#         print(f"{talaba.title()} baholandi")
#         baholangan_talabalar[talaba] = int(baho)
        
#     print(baholangan_talabalar)





