# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")


# salom_ber()


# def salom_ber(ism, familya):
#     """Fodyalanuvchi ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()} {familya.title()}!")

# salom_ber("hasan", "olimov")
# salom_ber("olim", "hakimov")

# 3
# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(
#         f"Foydalanuvchi ismi: {ism.title()}\n"
#         f"Foydalanuvchi familiyasi: {familiya.title()}"
#     )


# toliq_ism('olim','hakimov')


# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2022-tugilgan_yil} yoshda")


# yosh_hisobla('olim', 1997)
# # yosh_hisobla(1997,'olim')

# yosh_hisobla(tugilgan_yil=1997, ism="ali")
# # toliq_ism(familiya="hakimov", ism="olim")


# #4
# def yosh_hisobla(tugilgan_yil, joriy_yil=2022):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")


# yosh_hisobla(2005,2022)
# yosh_hisobla(1993, 2024)

# tyil = int(input("Tug'ilgan yilingizni kiriting: "))
# jyil = int(input("Joriy yilni kiriting: "))
# yosh_hisobla(tyil, jyil)
