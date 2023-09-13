# # 1-qism
# TARTIBLASH
cars = ["bmw", "mercedes benz", "volvo", "tesla", "audi"]
print(cars)
cars.sort() # a-z
print(cars)

harflar = ['p', 'z', 'o', 'b', 's', 'a', 'd']
print(harflar)
harflar.sort()
print(harflar)

# KATTA VA KICHIK HARF
cars = ['bmw', 'Volvo', 'gm', 'Tesla', 'Audi', 'a']
cars.sort()
print(cars)

# TESKARI TARTIB z-a
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
print(cars)
cars.sort(reverse=True)   # z - a; asl ro`yxatni o`zgartirib yuboradi 
print(cars)
print(sorted(cars))  # a -z; asl ro`yxatni o`zgartirmaydi 
print(cars)

# SORTED()
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() a-z dan qaytargan ro'yxat:", sorted(mehmonlar))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
print(sorted(mehmonlar, reverse=True))
print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)


# # SONLI RO'YXATLAR
# a = [12, 98, 34, 65, 34, 76, 11, 10.3, 23.32, 191_198_981_873]
# # a.sort() # a - z
# print(sorted(a))
# print(sorted(a, reverse=True))
# print(a)


# son1 = [9, 0, 4, 5, 2]
# son1.sort()
# print(son1)
# print(sorted(son1))


# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse() 
# print(fruits)

# son = [3, 5, 2, 1, 4]
# son.reverse() 
# print(son)



# # RO'YXAT UZUNLIGI
# fruits = ['pear','banana','apple','watermelon','lemon']
# print("Elementlar soni:", len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi

# # MIN(), MAX(), SUM()
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)
# print(f"Eng arzon narh: {arzon}. Eng qimmati: {qimmat}. Jami: {jami}")




# # masalalar










# friends = []
# name_1 = input("Ismingizni kiriting:  ")
# friends.append(name_1)
# name_2 = input("Ismingizni kiriting:  ")
# friends.append(name_2)
# name_3 = input("Ismingizni kiriting:  ")
# friends.append(name_3)
# name_4 = input("Ismingizni kiriting:  ")
# friends.append(name_4)
# name_5 = input("Ismingizni kiriting:  ")
# friends.append(name_5)
# print(sorted(friends))
# print(friends)







# # 2-qism

# # RANGE()
# sonlar = list(range(1, 10))
# print(sonlar)

# # RANGE VA QADAM          15, 35
# juft_sonlar = list(range(0, 20, 2)) # 0 dan 20 gacha 2 qadam bilan
# print("Juft sonlar: ", juft_sonlar)


# toq_sonlar = list(range(1, 20, 2))
# #toq_sonni chiqarib kurish
# print("Toq sonlar: ", toq_sonlar)

# # RO'YXATNI KESISH
# cars = ['bmw','mercedes benz', 'volvo', 
#         'general motors', 'tesla', 'audi']
# my_cars = cars[:4] # 0-indeskdan boshlab 3 ta element ajratib olamiz
# # print(cars)
# # print(my_cars)
# print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz
# print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi
# # print(cars)

# # RO'YXATDAN NUSXA OLISH
# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# # sonlar2 = sonlar
# sonlar2 = sonlar[:] # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.insert(0, 0) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)







# # TUPLES
# tomonlar = (3.14, 30, 55.2)
# tomonlar.append(0)
# del tomonlar[30]
# print(tomonlar)

# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[:5])

# toys = ('bus','car','bear','dino','snake','lizard')
# toys[3] = 'dragon'
# del(toys[0])
# toys.append('dragon')

# # TUPLES<->LIST
# toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# # Ro'yxatga o'zgartirishlar kiritamiz
# print(type(toys))
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(type(toys))
# print(toys)





# # masalalar


# numbers = list(range(22, 68))
# numbers_2 = numbers[:]
# numbers_2.append(88)
# numbers_2.append(12)
# numbers_2.append(0)
# numbers_2.append(99)
# print(f"Bu numbers list: {numbers}\n")
# print(f"Bu numbers_2 list: {sorted(numbers_2)}")
