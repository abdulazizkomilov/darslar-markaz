# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None): # args#     avto = {#         "kompany": kompaniya,#         "model": model,#         "color": rangi,#         "box": korobka,#         "year": yili,#         "price": narhi,#     }#     return avto# a1 = avto_info("gm", 'matiz', 'oq','mexanika', 2020, 3000)# avto_test = avto_info("GM", "Nexia", "oq", "avto", 2020) # avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2018, 20000)# avto2 = avto_info("GM", "Gentra", "Oq", "Mexanika", 2019, 15000)# avtolar = [a1, avto_test, avto1, avto2]# print("Onlayn bozordagi mavjud avtomashinalar: ")# for avto in avtolar:#     if avto["price"]:#         narx = f'{avto["price"]}$'#     else:#         narx = "Noma'lum"#     print(f"{avto['color'].capitalize()} {avto['model']}. Narxi: {narx}")            # def oraliq(min, max):#     sonlar = []#     while min < max:#         sonlar.append(min)#         min += 1#     return sonlar# print(oraliq(0,10))# print(oraliq(10, 21))# def oraliq(min, max, step=1):#     sonlar = []#     while min < max:#         sonlar.append(min)#         min += step#     return sonlar# print(oraliq(0, 21, 2))# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")# avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat# while True:#     print("\nQuyidagi ma'lumotlarni kiriting", end=" ")#     kompaniya = input("Ishlab chiqaruvchi: ")#     model = input("Modeli: ")#     rang = input("Rangi: ")#     korobka = input("Korobka: ")#     yil = input("Ishlab chiqarilgan yili: ")#     narh = input("Narhi: ")#     avtolar.append(avto_info(kompaniya, model, rang, korobka, yil, narh))#     javob = input("Yana avto qo'shasizmi? (yes/no): ")#     if javob == "no":#         break            # print("\nSalonimizdagi avtolar:")# for avto in avtolar:#     if avto["price"]:#         narh = f"{avto['price']}$"#     else:#         narh = "Noma'lum"#     print(#         f"{avto['year'].title()} {avto['model'].title()}, "#         f"{avto['box']} korobka. Narhi: {narh}"#     )