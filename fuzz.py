from fuzzywuzzy import fuzz
from fuzzywuzzy import process

words = ['talaba', 'tolib', 'kasalxona', 'tatil', 'salat', "salim", "salom",'assalom']

# # # ikki so'z 'ortasida o'xshashlik foizini topish
# print(fuzz.ratio("salom",'assalom'))
# print(fuzz.ratio("salom","salim"))

# # Matnlar orasidan 3 ta eng o'xshashlarini ajratib olish
# text = "salom"
# matches = process.extract(text, words, limit=3)
# print(matches)

# # # Matnlar orasidan eng o'xshashini topish
# text = "kasalhona"
# match = process.extractOne(text, words)
# print(match)