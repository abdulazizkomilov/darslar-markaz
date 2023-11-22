# 1-masala

# Istalgan son kiritilsa kiritilgan 
# songacha bo`lgan toq sonlar 
# yigindisini hisoblang

# >>> 7
# 1, 2, 3, 4, 5, 6, 7
# son = int(input("Istalgan son kiriting: "))
# sonlar = list(range(1, son+1))
# yigindi = 0
# for a in sonlar:
#     if a % 2 == 1:
#         yigindi += a #  yigindi = yigindi + a 
# print('Natija: ', yigindi)




# son = int(input("Istalgan son kiting va men shu songacha bo'gan toq sonlar yigindisini hisoblayman.\n>>>  "))
# sonlar = list(range(1, son+1))
# yigindi = 0

# for i in sonlar:
#     if i % 2 == 1:
#         yigindi+=i
# print('Yig`indi: ',yigindi)


# # 2.1
# # formula: S = a * b

# To`g`ri to`rtburchakning yuzasini 
# hisoblash dasturini tuzing.
# Yechim: 𝑆 = 𝑎 ∙ 𝑏;
# bu yerda a-to`g`ri to`rtburchakning eni, 
# b-to`g`ri to`rtburchakning bo`yi.

# a = float(input('t.t.enini k.:  '))
# b = float(input('t.t.buyini k.: '))
# S = a * b
# print(f"S = a • b ning yuzasi {S} m2 ga teng")


# 2.2
# Radiusi berilgan doiraning yuzasi va 
# uzunligini hisoblash dasturini tuzing.
# Yechim: 𝑆 = 𝜋 ∙ 𝑟2, 𝑙 = 2𝜋𝑟;  r2 -- r ** 2
# bu yerda, r-doira radiusi.

# r = float(input('Radiusni kiriting: '))
# from math import pi
# s = pi * r ** 2
# l = 2 * pi * r
# print('yuza: ', round(s), 'uzunlik: ', round(l))



# 2.4-masala
# Asosi va balandligi berilgan 
# uchburchakning yuzasini topish 
# dasturini tuzing.

# Yechim: 𝑆 = 1/2 * a * h
# bu yerda, a - uchburchakning asosi, 
# h - uchburchakning balandligi.




# 2.5-masala   
# Kiritilgan butun tipdagi n sonni 
# n+nn+nnn ko`rinishida hisoblash 
# dasturini tuzing.
# Masalan, n=5 -> 5+55+555=615.




# 1.0
# ... >> 3.5

# 2.6-masala
# 1 dan N gacha musbat butun songacha 
# bo`lgan sonlarning yig`indisini
# hisoblash dasturini tuzing.
# 1-usul: arifmetik progressiyani qo`llash.
# Yechim: 
# 𝑆 = (𝑎1+𝑎𝑛) / 2 * 𝑛
# bu yerda 𝑎1 = 1 va 𝑎𝑛
# = 𝑛 ga teng.

# a1 = int(input('a1 k.:  '))
# an = int(input('an k.: '))
# s = (a1+an) / 2 * an
# print(f"S = (𝑎1+𝑎𝑛) / 2 * 𝑛 ning a. p. {s}")


# VAZIFA
# 1.0
# 2.7 >> 3.5




# Amallardan birini tanlang va men sizga shu amalga doir 5ta misol beraman (+), (-), (x), (/) 