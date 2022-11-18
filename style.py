davlatlar = {
    "o'zbekiston": "toshkent",
    "aqsh": "washington d.c.",
    "rossiya": "moskva",
    "tojikiston": "dushanbe",
    "qirg'iziston": "bishkek",
    "qozog'iston": "nursulton",
    "malayziya": "kuala-lumpur",
    "singapur": "singapur",
    "italiya": "rim",
}

country = input("Qaysi davlatning poytaxtini bilishni istaysiz?:").lower()
capital = davlatlar.get(country)
if capital == None:
    print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
