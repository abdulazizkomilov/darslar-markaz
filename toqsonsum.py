print("  Istalgan songacha bulgan toq sonlar yig'indisini hisoblaydi \n")
son = 0
l = 0
son1 = [ ]
b = ' '
g = int(input('  Son kiriting:  '))
for a in range(1, g + 1):
	l = l+a
	if a %2 == 0:
		continue
	else:
		b = son + a
		son1.append(b)
		
d = sum(son1)
print(f"  Toq sonlar ruyxati {son1} \n")
print(f"  {g} gacha bulgan toq sonlar yig'indisi {d} ga teng.\n  Raxmat dasturimizdan foydalanganigiz uchun! ")