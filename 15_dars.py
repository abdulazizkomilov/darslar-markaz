# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n = 1  # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n += 1
#     if takrorlash != "ha":
#         break
    
# print("Do'stlaringiz ro'yxati: ")
# for ism in ismlar:
#     print(ism.title())
    
    
    
# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# n = 1
# while ishora:
#     ism = input(f"{n} - do'stingiz ismini kiriting: ")
#     yosh = int(input(f"{ism.title()}ning yoshini kiriting: "))
#     dostlar[ism] = yosh
#     n+=1
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob != "ha":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")
    
    
    
cars = ["lacetti", "nexia", "toyota","nexia", "audi", "malibu", "nexia", "lacetti"]
car = ["nexia", "lacetti"]

while car: # 1ta, 1ta
    
    i = car.pop()
    
    while i in cars:  # 3ta, 2ta
        cars.remove(i)
        
print(cars)


# talabalar = ["hasan", "husan", "olim", "botir"]
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)



