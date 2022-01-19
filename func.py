# # oddiy fun()
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")


# salom_ber()


# # 2
# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")


# # salom_ber("hasan")
# # salom_ber("olim")

# salom_ber()



# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab 
#     chiqaruvchi funksiya"""
#     print(
#         f"Foydalanuvchi ismi: {ism.title()}\n"
#         f"Foydalanuvchi familiyasi: {familiya.title()}"
#     )


# toliq_ism('olim','hakimov')
# # toliq_ism('hakimov','olim')



# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2021-tugilgan_yil} yoshda")


# # yosh_hisobla('olim', 1997)
# # yosh_hisobla(1997, 'olim')

# # yosh_hisobla(ism='olim', tugilgan_yil=1997)
# # toliq_ism(familiya="hakimov", ism="olim")


# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     """Foydalanuvchi tug'ilgan yilidan uning 
#     yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")


# # yosh_hisobla(1995, 2021)
# # yosh_hisobla(1993)

# t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh_hisobla(t_yil, 2030)

# def toliq_ism_yasa(ism, familiya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism


# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "olimov")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# print(f"{talaba1} darsga kechikib keldi")