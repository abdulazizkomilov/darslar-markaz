class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
    
class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        
    def __repr__(self):
        info = f"{self.ism} {self.familiya} "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya} "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

shaxs1 = Shaxs("olim", "karimov", "AB3457261", 1997)
shaxs2 = Shaxs("vali", "kamolov", "BC7922639", 1980)

talaba = Talaba("olim", "karimov", "AB3457261", 1997, "ID56782", "yangiyer")
talaba1 = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012", "samarqand")

class Manzil:
    """Manzil saqlash uchun klass"""

    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
        
    def __repr__(self):
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil

talaba1_manzil = Manzil(12, "Olmazor", "Bog'bon", "Samarqand")
talaba2 = Talaba("Valijon", "Aliyev", "FA112299", 2000, "0000012", talaba1_manzil)




class University:
    def __init__(self, name):
        """Manzil xususiyatlari"""
        self.name = name
        self.students_list = []
        self.students_nums = 0
        
    def __repr__(self):
        return f"{self.name} universiteti"

    def __len__(self):
        return len(self.students_list)

    def __getitem__(self, index):
        return self.students_list[index]

    def __setitem__(self, index, value):
        if isinstance(value, Talaba):
            self.students_list[index] = value

    def __add__(self, qiymat):     # salon3 = salon1 + salon2 / salon1 + avto6
        if isinstance(qiymat, University):
            yangi_uni = University(f"{self.name} {qiymat.name}")
            yangi_uni.students_list = self.students_list + qiymat.students_list
            return yangi_uni
        elif isinstance(qiymat, Talaba):
            self.add_student(qiymat)
        else:
            print(f"Universitetga {type(qiymat)} qo`shib bo`lmaydi")

    def __call__(self, *param):
        if param:
            for student in param:
                self.add_student(student)
        else:
            return [student for student in self.students_list]

    def add_student(self, *qiymat):
        for student in qiymat:
            if isinstance(student, Talaba):
                self.students_list.append(student)
            else:
                print("Talaba obyketini kiriting")

    def get_list(self):
        return [student for student in self.students_list]




uni1 = University("TATU")
uni2 = University("SAMDU")
uni3 = University("INHA")


uni1.add_student(talaba, talaba1)
uni2(talaba2)

