# file = open("pi.txt")
# PI = file.read()
# # print(PI)
# file.close()


#yopilishi
with open("pi.txt") as file:
    pi = file.read()

print(pi)

# pi = pi.rstrip()
# pi = pi.replace("\n", "")
# pi = float(pi)
# print(pi)


# filename = "data/talabalar.txt"
# with open(filename) as file:
#     for line in file:
#         print(line)

# # ro`yxat ichiga saqlash
# with open(filename) as file:
#     talabalar = file.readlines()

# print(talabalar)

# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)



# # #yozish  "W" write ustidan yozib yuboradi
# faylnomi = "new_file.txt"
# ism = "Umar Hasanov"
# tyil = 1999
# with open(faylnomi, "w") as fayl:
#     fayl.write(ism + "\n")
#     fayl.write(str(tyil) + "\n")

# #qo`shish yoki yangi yasash "a" append
# with open(faylnomi, "a") as fayl:
#     fayl.write("Alijon Valiyev\n")
#     fayl.write("2000")


# import pickle

# talaba1 = {"ism": "hasan", "familiya": "husanov", "tyil": 2003, "kurs": 2}
# talaba2 = {"ism": "alijon", "familiya": "valiyev", "tyil": 2004, "kurs": 1}

# # datalarni yozish wr - write binary  // ko`rib bo`lmaydi editorda
# with open("info", "wb") as file:
#     pickle.dump(talaba1, file)
#     pickle.dump(talaba2, file)
    

# # # datani o`qish rb - read binary  // 2lik sanoq sistemada
# # import pickle

# with open("info", "rb") as file:
#     talaba_1 = pickle.load(file)
#     talaba_2 = pickle.load(file)

# print(talaba_1)
# print(talaba_2)