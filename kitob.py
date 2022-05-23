kitoblar = {
    'a':1000,
    'b':2000,
    'c':3000
}
kitob_f = []
while True:
    savol = input("Ol. Bo`. Ki. Ki.\'exit' >>>  ")
    if savol == "exit":
        break
    else:
        kitob_f.append(savol)
for kitob in kitob_f:
    print(f"Kitoblar:{kitoblar[kitob]}")

    