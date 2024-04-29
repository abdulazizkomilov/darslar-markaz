# docs.python.org/3/library

# import datetime as dt

# # # datetime()
# hozir = dt.datetime.now()
# print(hozir)
# # # sanani ajratib olish
# print(hozir.date())
# # # vaqtni ajratib olish
# print(hozir.time())
# # # soatni ajratib olish
# print(hozir.hour)
# # # minutni ajratib olish
# print(hozir.minute)
# # # # sekundni ajratib olish
# print(hozir.second)


# # date()           yil   oy kun
# tugulgan = dt.date(2008, 1, 1)
# print(f"tugulgan sana: {tugulgan}")
# bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")
# print(bugun - tugulgan)







# # time()
# hozir = dt.datetime.now()
# vaqtHozir = hozir.time()
# print(f"Hozir soat: {vaqtHozir}")
# vaqtKeyin = dt.time(23, 45, 30)
# print(vaqtKeyin)






# # Sanalar orasida farq
# bugun = dt.date.today()
# tatil = dt.date(2024, 5, 25)
# farq = tatil - bugun
# print(f"Ta`tilga {farq.days} kun qoldi")





# # Soatlar orasida farq
# hozir = dt.datetime.now()
# #                      yil   oy kun  h  m   s
# tugulgan = dt.datetime(2007, 10, 28, 2, 00, 00)
# farq = hozir - tugulgan
# sekundlar = farq.seconds
# minutlar = int(sekundlar / 60)
# soatlar = int(minutlar / 60)
# print(f"Yashagan vaqt: {farq.days} kunu {soatlar} soat")





# # Vatqni formatlash
# hozir = dt.datetime.now()
# vaqt = hozir.strftime("%H:%M:%S")
# print(f"Hozir soat: {vaqt}")


# sana = hozir.strftime("%d-%m-%Y")
# print(f"Bugun sana: {sana}")


# hozir = dt.datetime.now()
# sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
# print(sana_vaqt)




# from datetime import datetime, timedelta

# def get_first_day_of_next_month():
#     # Joriy sana
#     current_date = datetime.now()

#     # Keyingi oyning boshlanish kunini olish
#     if current_date.month == 12:
#         next_month_start = datetime(current_date.year + 1, 1, 1)
#     else:
#         next_month_start = datetime(current_date.year, current_date.month + 1, 1)

#     return next_month_start

# # Mavjud sana vaqtini olish
# next_month_start_date = get_first_day_of_next_month()
# print(next_month_start_date)

