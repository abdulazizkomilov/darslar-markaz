# # friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga 
# # chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append("John")
friends.append("Alex")
friends.append("Danny")
friends.append("Sobirjon")
friends.append("Vanya")
# print(f"To`liq list-{friends}")

# # # # Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
# friends.remove("John")
# friends.remove("Alex")
# friends.remove("Vanya")
# print(f"Kelganlar-{friends}")

# # # Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append("Hasan")
friends.insert(0, "Husan")
friends.insert(2, "Ivan")
# friends.insert(3, 90)
# print(friends)

# # Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))

print("\nKelgan mehmonlar: ", mehmonlar)












