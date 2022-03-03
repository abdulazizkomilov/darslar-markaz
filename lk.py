mahsulotlar = ["un","yog'","sovun","tuxum","piyoz","kartoshka","olma","banan","uzum","qovun"]

savat = []
for x in range(1,6):
    ask = input(f"{x} - mahsulotni kiriting>>> ")
    savat.append(ask)
    
for a in mahsulotlar:
    if a not in savat:
        print(f"{a} bizda yuq, iltimos dukonga {a} olib keling!")
    else:
        print(f"{a} savatingizda bor")
        