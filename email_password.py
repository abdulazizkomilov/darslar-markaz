# ihateregex.io site

import re  # RegEx == Regular Expression

# word1 = "temir"
# word2 = "tomir"
# word3 = "tulpor"

# andoza = "^t...r$"

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))

# words = ['olma', 'olcha', 'olim', 'ol', 'hakam', 'otliq']
# andoza = "^o..a$"
# matches = []
# for word in words:
#     if re.match(andoza, word):
#         matches.append(word)

# print(matches)

# ## Emailni ajratib olish
# matn = """ Maqolalar  2020-yilning 20-martiga qadar ferensiya2021@gmail.com / jecolen@gmail.com elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

# andoza = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
# email = re.findall(andoza, matn)
# print(email)

# Kuchli parolni tekshirish
andoza = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"
msg = "Yangi parol kiriting"
msg += "(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, "
msg += "1 ta son va 1 ta maxsus belgi boʻlishi kerak): "

while True:
    password = input(msg)
    if re.match(andoza, password):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi")