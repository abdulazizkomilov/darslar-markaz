# #Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#   if car=='gm':
#     print(car.upper())
#   else:
#     print(car.title())
    

# #Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#   if car!='gm':
#     print(car.title())
#   else:
#     print(car.upper()) 
    
    
# #Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks xolda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
# login = input("Login kiriting: ")
# if login.lower() == 'admin':
#   print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#   print(f"Xush kelibsiz {login.title()}!")
  
# #Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting:"))
# if x==y: print(f"Sonlar teng: {x}={y}")

# #Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
# son = float(input("Istalgan son kiriting:"))
# print("Son manfiy") if son<0 else print("Son musbat")


# #Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
# son = float(input('Istalgan son kiriting: '))
# print(son**(1/2)) if son>0 else print('Musbat son kiriting')