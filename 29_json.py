import json
# JSON (JavaScript Object Notation).

 # indent=4
# x = 10
# x_json = json.dumps(x)

# y = 5.5
# y_json = json.dumps(y)

# m = True
# m_json = json.dumps(m)

# familiya = "alimov"
# familiya_json = json.dumps(familiya)
# ism_json = json.dumps('olimbek')

sonlar = (12, 45, 23, 67)
# sonlar_json = json.dumps(sonlar)


# # python file qaytarish
# son2 = json.loads(sonlar_json)




bemor = {
    "ism": "Alijon Valiyev",
    "yosh": 30,
    "oila": True,
    "farzandlar": ("Ahmad", "Bonu"),
    "allergiya": None,
    "dorilar": [
        {"nomi": "Tremol", "miqdori": 0.5},
        {"nomi": "Panadol", "miqdori": 1.2},
    ],
}

# bemor_json = json.dumps(bemor)
# print(bemor_json)

#yozish
with open("bemor_j.json", "w") as f:
    json.dump(bemor, f)


with open("sonlar_j.json", "w") as f:
    json.dump(sonlar, f)


filename = "bemor_j.json"
with open(filename) as f:
    bemor = json.load(f)
print(bemor)
print(type(bemor))

