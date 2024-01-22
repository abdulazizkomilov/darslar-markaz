# pip install googletrans==3.1.0a0
from googletrans import Translator

tarjimon = Translator()

# msg = input('Tarjima uchun so\'z kiriting (chiqib ketish uchun "q" deb yozing): ')

# tarjima = tarjimon.translate(msg, dest='en')
# print(tarjima.text)


til1 = tarjimon.detect('이 문장은 한글로 쓰여졌습니다.')
til2 = tarjimon.detect('This sentence is written in English.')
til3 = tarjimon.detect('Tiu frazo estas skribita en Esperanto.')
print(til1)
print(til2)
print(til3)
