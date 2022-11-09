# 1
import math as m
a = int(input("a ni kiriting>>>  "))
b = int(input("b ni kiriting>>>  "))
c = int(input("c ni kiriting>>>  "))
yigindi = (1/2)*(m.sqrt(((b**2) + (c**2) + 2*b*c * m.cos(a))))
print(yigindi)

# 2
class Uzgaruvchi():
    """Sonlar ma'lumoti"""
    def __init__(self, son_1, son_2):
        """Sonlar"""
        self.son_1 = son_1
        self.son_2 = son_2

    def get_sum(self):
        """Sonlar yigindisi"""
        summa = f"Ikki sonning yigindisi: {int(self.son_1) + int(self.son_2)}"
        return summa
    def get_max(self):
        """Katta son"""
        son = max(self.son_1, self.son_2)
        maximum = f"Ikki sondan kattasi {son}"
        return maximum

sonlar1 = Uzgaruvchi(2000, 3000)
sonlar2 = Uzgaruvchi(2400, 5600)

print(sonlar1.get_sum())
print(sonlar1.get_max())
print(sonlar2.get_sum())
print(sonlar2.get_max())


