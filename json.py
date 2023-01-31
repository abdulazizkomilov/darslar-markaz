import json
# JSON (JavaScript Object Notation).

 # indent=4
x = 10
x_json = json.dumps(x)

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)

# # ism = "anvar"
# # ism_json = json.dumps(ism)
# # familiya_json = json.dumps('narzullaev')

# sonlar = (12, 45, 23, 67)
# sonlar_json = json.dumps(sonlar)

# bemor = {
#     "ism": "Alijon Valiyev",
#     "yosh": 30,
#     "oila": True,
#     "farzandlar": ("Ahmad", "Bonu"),
#     "allergiya": None,
#     "dorilar": [
#         {"nomi": "Analgin", "miqdori": 0.5},
#         {"nomi": "Panadol", "miqdori": 1.2},
#     ],
# }

# bemor_json = json.dumps(bemor)
# print(bemor_json)

# #yozish
# with open("sonlar.json", "w") as f:
#     json.dump(sonlar, f)


# # python file qaytarish
# bemor2 = json.loads(sonlar_json)
# print(bemor2)

# filename = "sonlar.json"
# with open(filename) as f:
#     bemor = json.load(f)
# print(bemor)
# print(type(bemor))

