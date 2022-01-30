import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
print(rate)                        #printing current voice rate
engine.setProperty('rate', 125)
engine.say(" if bog'lovchisi qatnashgan shartli gaplarni guruhlarga boʻlib oʻrganish tavsiya qilinadi. Qavs ichida bu gaplarning real (haqiqatga toʻg'ri keladigan) va noreal (haqiqatga toʻg'ri kelmaydigan) vaziyatlar uchun qoʻllanishi berilgan.")
engine.runAndWait()