# # RANGE()
# sonlar = list(range(1, 10))
# print(sonlar)

# # RANGE VA QADA          15, 35
# juft_sonlar = list(range(0, 200, 2)) # 0 dan 20 gacha 2 qadam bilan
# print("Juft sonlar: ", juft_sonlar)


# toq_sonlar = list(range(1, 20, 2))
# #toq_sonni chiqarib kurish
# print("Toq sonlar: ", toq_sonlar)

# # RO'YXATNI KESISH
# cars = ['bmw','mercedes benz', 'volvo', 
#         'general motors', 'tesla', 'audi']
# my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
# print(cars)
# print(my_cars)
# print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz
# print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi
# print(cars)

# # RO'YXATDAN NUSXA OLISH
# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# # sonlar2 = sonlar
# sonlar2 = sonlar[:] # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)


# numbers deb nomlangan list yasang va range yordamida 
# 22dan 68gacha sonlarni shakillantirib oling va 
# shu listdan numbers_2 nomli list yasab unga qo`shimcha 
# # 88, 12, 0 va 99 sonlarni qo`shib tartib bilan chiqaring
# numbers = list(range(22, 68))
# numbers_2 = numbers[:]
# numbers_2.append(88)
# numbers_2.append(12)
# numbers_2.append(0)
# numbers_2.append(99)
# print(f"Bu numbers list: {numbers}\n")
# print(f"Bu numbers_2 list: {sorted(numbers_2)}")

# son1 = [9, 0, 4, 5, 2]
# # son1.sort()
# # print(son1)
# print(sorted(son1))

# # TUPLES
# tomonlar = (3.14, 30, 55.2)
# # tomonlar.append(0)
# # del tomonlar[30]
# print(tomonlar)

# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[:5])

# toys = ('bus','car','bear','dino','snake','lizard')
# toys[3] = 'dragon'
# del(toys[0])
# toys.append('dragon')

# TUPLES<->LIST
toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)
