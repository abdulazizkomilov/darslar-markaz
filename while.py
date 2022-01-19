# # while()
# son = 1  # son ga 1 qiymatini beramiz
# while son <= 5:  # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=" ")  # son ni konsolga chiqaramiz
#     son = son + 1
#     # son += 1 # songa 1 qo'shamiz

# son1 = 0 
# while True:
#     print(f"{son1}")
#     son1 += 1

# # while and input
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print('Dastur tugadi')


# # ishora
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print('Dastur to\'xtadi!')

# print("Ro`yxat qabul qiluvchi dastur.")
# savol = "Bozorlik ro`yxatini kiriting "
# savol += "(dasturni to'xtatish uchun 'enter' tugmasini bosing): "
# bozorliklar = []
# ishora = True
# while ishora:
#     bozorlik = input(savol)
#     bozorliklar.append(bozorlik)
#     if bozorlik == '':
#         ishora = False

# print("Sizning ro`yxat: ")
# for bozorlik1 in bozorliklar:
#     print(bozorlik1.capitalize(), end=" ")
    
# print('\nBozorlik qabul qilindi, Raxmat!')
    
    

# # break while
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi!')
# # break for

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# # CONTINUE
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# # Continue while
# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# # infinite loop
# son = 0
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# son = 0
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)
#     son += 1

# son = 1
# while son>0:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)