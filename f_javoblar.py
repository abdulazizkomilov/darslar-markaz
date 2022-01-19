# # Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def kv_kub(son):
#     """Kiritilgan sonning kvadrati va kubini konsolga chiqaruvchi funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga, kubi {son**3} ga teng")


# kv_kub(-4)


# # Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# def juftmi(son):
#     """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     if son % 2:
#         print(f"{son} toq son")
#     else:
#         print(f"{son} juft son")


# juftmi(20)
# juftmi(123)


# # Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
# # Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def daraja(x, y=2):
#     print(f"{x} ning {y}-darajasi {x**y} ga teng")


# daraja(5, 2)
# daraja(3, 3)
# daraja(94, 4)
# daraja(6)

# # Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
# def daraja(x, y):
#     """x ni y-darajaga oshiruvchi funksiya"""
#     print(f"{x} ning {y}-darajasi {x**y} ga teng")


# daraja(5, 2)
# daraja(3, 3)
# daraja(94, 4)


# # Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
# # Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def daraja(x, y=2):
#     print(f"{x} ning {y}-darajasi {x**y} ga teng")


# daraja(5, 2)
# daraja(3, 3)
# daraja(94, 4)
# daraja(6)


# Foydalanuvchidan son qabul qilib, sonni 2, 3, 4 va 5 ga qoldiqsiz bo'linishini tekshiruvchi
# funksiya yozing.
# Natijalarni konsolga chiqaring ("15 soni 3 ga qoldiqsiz bo'linadi" ko'rinishida)
def bolinish_alomatlari(son):
    for n in range(2, 11):
        if son % n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")
            



bolinish_alomatlari(20)