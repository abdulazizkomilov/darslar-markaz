from random import *  ##  tasodifiy son yoki harfni tanlash
tahmin = ""
parol = input("Buziladigan parolnni kirting:  >> ")
harflar = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","q","r","s","t","u","w","x","v","z","y"]
while(tahmin !=parol):
    tahmin = ""
    for harf in range(len(parol)):
        tahmin_harf=harflar[randint(0, len(parol))]
        tahmin=str(tahmin_harf) + str(tahmin)
        print(tahmin)      
tugatish = input(f"Parol:<<{tahmin}>>   Dasturdan chiqiw uchun istalgan tugamngizni bosing ")