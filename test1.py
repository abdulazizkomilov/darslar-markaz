# 1
son = input("Istalgan son kiiting: ")
a = int(son[0:1])
b = int(son[1:2])
c = int(son[2:])

print(f"{a} + {b} + {c} = {a+b+c}")

# 2
class Mashina():
    """Mashina haqida ma'lumot"""
    def __init__(self, model, rang, yil, masofa):
        """Mashinaning xususiyatlari"""
        self.model = model
        self.rang = rang
        self.yil = yil
        self.masofa = masofa

    def get_info(self):
        """Mashina haqida ma'lumot"""
        if self.masofa > 0:
            info = f"Mashina markasi {self.model}, rangi {self.rang}, "
            info += f"ishlab chiqarilgan yil {self.yil}, bosib o`tgan masofasi {self.masofa}km."
        else:
            info = f"Mshaina markasi {self.model}, rangi {self.rang}, "
            info += f"ishlab chiqarilgan yil {self.yil}, Mashina yurmagan hali yangi."
        return info

mashina1 = Mashina('Nexia', 'oq', 2008, 30000)
mashina2 = Mashina('Kaptiva', 'qora', 2019, 10000)
mashina3 = Mashina('Gentira', 'oq', 2022, 0)

print(mashina1.get_info())
print(mashina2.get_info())
print(mashina3.get_info())

