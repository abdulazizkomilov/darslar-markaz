# 1
son = input("Istalgan son kiiting: ")
a = int(son[0:1])
b = int(son[1:2])
c = int(son[2:3])
d = int(son[3:])

print(f"{a} x {b} x {c} x {d} = {a*b*c*d}")

# 2
class Talaba:
    """Talaba klassi"""

    def __init__(self, ism, familiya, manzil, kurs):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.kurs = kurs
        self.manzil = manzil

    def get_id(self):
        """Talabaning ismi"""
        return self.ism

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.kurs

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"Talabaning ismi {self.ism.title()} {self.familiya.title()}. "
        info += f"{self.get_bosqich()}-kurs talabasi. Manzil: {self.manzil.title()}"
        return info

shaxs1 = Talaba("olim", "karimov", "samarqand", 2)
shaxs2 = Talaba("vali", "hakimov", "sirdaryo", 4)
shaxs3 = Talaba("ali", "alimov", "tashkent", 1)
print(shaxs1.get_info())
print(shaxs2.get_info())
print(shaxs3.get_info())

