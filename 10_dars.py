# def toliq_ism_yasa(ism, familiya): # args - parms
#     """..."""
#     toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism

# talaba1 = toliq_ism_yasa("husan", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "husanov")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# print(f"{talaba1} darsga kechikib keldi")




# def toliq_ism_yasa(ism, familiya, o_ismi="", yosh=0):
#     """..."""
#     if o_ismi and yosh:
#         toliq_ism = f"{ism} {o_ismi} {familiya}, {yosh}-yosh da"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa("g`ani", "jamolov")
# talaba2 = toliq_ism_yasa("hakim", "kamolov", "abrorovich", 37)
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")






# def friends_list():
#     """..."""
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
        


# 1 - kitob:  grokking
# grokking narxi: 40000

# ...

# ...


# Kitoblar:
#     1. grokking - 40000
#     2. ........ - 39000




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
# friends_list_data()


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

# set_ball()

