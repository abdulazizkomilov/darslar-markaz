# file = open("pi.txt")
# PI = file.read()
# print(PI)
# file.close()


# # yopilishi
# with open("pi.txt") as file:
#     pi = file.read()
    
# # print(pi)

# pi = pi.rstrip()  #yangi qatorni olib tashlaydi
# pi = pi.replace('\n', "")  #o`rniga almashtiradi
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
#     fayl.write(ism + '\n')
#     fayl.write(str(tyil) + '\n')

#qo`shish yoki yangi yasash "a" append
# with open(faylnomi, "a") as fayl:
#     fayl.write("Alijon Valiyev\n")
#     fayl.write("2000")


import pickle

talaba1 = {"ism": "hasan", "familiya": "husanov", "tyil": 2003, "kurs": 2}

# datalarni yozish wr - write binary  // ko`rib bo`lmaydi editorda
with open("info1", "wb") as file:
    pickle.dump(talaba1, file)
    
# datani o`qish rb - read binary  // 2lik sanoq sistemada
with open("info1", "rb") as file:
    talaba_1 = pickle.load(file)

print(talaba_1)