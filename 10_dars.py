# def toliq_ism_yasa(ism, familiya): # args - parms
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism

# talaba1 = toliq_ism_yasa("husan", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "husanov")

# print(f"Darsga kelmagan talabalar: {talaba1}"
#       f"va {talaba2}")
# print(f"{talaba1} darsga kechikib keldi")






def toliq_ism_yasa(ism, familiya, o_ismi=""):     # args - parms
    if o_ismi: 
        toliq_ism = f"{ism} {familiya} {o_ismi} "
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism

talaba1 = toliq_ism_yasa("husan", "jamolov")
talaba2 = toliq_ism_yasa("hakim", "kamolov", "olim o'g'li.")

print(f"Darsga kelmaganlar: {talaba1} va {talaba2}")




# def friends_list():
#     print("Ismlar ro'yxatini tuzamiz.")
#     ismlar = []
#     n = 1 
#     while True:
#         savol = f"{n}-ismini kiriting: "
#         ism = input(savol)
#         ismlar.append(ism)
#         takrorlash = input("ism qo'shasizmi? (ha/yo'q)")
#         n += 1
#         if takrorlash != "ha":
#             break     
#     print("Ismlar: ")
#     for ism in ismlar:
#         print(ism.title(), end=" ")
# friends_list()
        


# []  {"grokking": 40000}
# 1 - kitob:  grokking
# grokking narxi: 40000

# Kitoblar:
#     1. grokking - 40000
#     2. ........ - 39000

# dic = {'grokking': 1000}
# dic[name] = price




# def books_list():
#     print("Enter books: ")
#     books = {}
#     while True:
#         name = input("enter name: ")
#         price = int(input(f"{name} price: "))
#         books[name] = price
#         takrorlash = input("kitob qo'shasizmi? (ha/yo'q)")
#         if takrorlash != "ha":
#             return books 

# print(books_list())




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
#     talabalar = ["hasan", "husan", "olim", "botir"]
#     baholangan_talabalar = {}
#     while talabalar:
#         talaba = talabalar.pop()
#         baho = input(f"{talaba.title()}ni baholang: ")
#         print(f"{talaba.title()} baholandi")
#         baholangan_talabalar[talaba] = int(baho)
        
#     print(baholangan_talabalar)

# set_ball()

