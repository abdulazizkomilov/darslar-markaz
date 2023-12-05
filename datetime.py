# docs.python.org/3/library

import datetime as dt
# # datetime()
# hozir = dt.datetime.now()
# print(hozir)
# # sanani ajratib olish
# print(hozir.date())
# # vaqtni ajratib olish
# print(hozir.time())
# # soatni ajratib olish
# print(hozir.hour)
# # minutni ajratib olish
# print(hozir.minute)
# # # sekundni ajratib olish
# print(hozir.second)

# # date()
# bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")
# ertaga = dt.date(2022, 12, 19)
# print(f"Ertangi sana: {ertaga}")

# # time()
# hozir = dt.datetime.now()
# vaqtHozir = hozir.time()
# print(f"Hozir soat: {vaqtHozir}")
# vaqtKeyin = dt.time(23, 45, 30)
# print(vaqtKeyin)

# # Sanalar orasida farq
# bugun = dt.date.today()
# tatil = dt.date(2022, 12, 24)
# farq = tatil - bugun
# # print(farq)
# print(f"Ta`tilga {farq.days} kun qoldi")

# # # Soatlar orasida farq
# hozir = dt.datetime.now()
# futbol = dt.datetime(2022, 12, 19, 00, 00, 00)
# farq = futbol - hozir
# sekundlar = farq.seconds
# minutlar = int(sekundlar / 60)
# soatlar = int(minutlar / 60)
# print(f"""Futbol tugashiga {farq.days} kunu
#       {soatlar} soat qoldi""")

# # Vatqni formatlash
# hozir = dt.datetime.now()
# vaqt = hozir.strftime("%H:%M:%S")
# print(f"Hozir soat: {vaqt}")

# sana = hozir.strftime("%d-%m-%Y")
# print(f"Bugun sana: {sana}")

# sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
# print(sana_vaqt)


from datetime import datetime, timedelta

def get_first_day_of_next_month():
    # Joriy sana
    current_date = datetime.now()

    # Keyingi oyning boshlanish kunini olish
    if current_date.month == 12:
        next_month_start = datetime(current_date.year + 1, 1, 1)
    else:
        next_month_start = datetime(current_date.year, current_date.month + 1, 1)

    return next_month_start

# Mavjud sana vaqtini olish
next_month_start_date = get_first_day_of_next_month()




current_date = dt.datetime.now()
y = current_date.year
m = current_date.month
d = current_date.day


if m == 12:
    next_pay = datetime(y + 1, 1, d)
else:
    next_pay = datetime(y, m + 1, d)


next_date = dt.datetime(2024,1,4)
if next_date == next_pay:
    print('tolov')
else:
    print("ok")


