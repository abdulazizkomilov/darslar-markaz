import re  # RegEx == Regular Expression

talabalar = {
    '1' : {
        'abbos abdusalomov': 'hg',
        'husan kamolov': 'jk',
        'jalol hakimov': 'lk'
        },
    '2': {
        'yusuf umarov': 'jh',
        'elbek rustamov': 'sd',
        'feruza jamolova': 'ew'
        },
    '3': {
        'salim olimov': 'sd',
        'oybek sobirov': 'qw',
        'utkir latipov': 'tr'
        },
    '4': {
        'zayid numonov': 'op',
        'ilyos saddamov': 'ds',
        'molik jamolov': 'dw'
        }
    }

kurs = input(".>>>  ")
andoza = input('>>>  ')
matches = {}
for word in talabalar.keys():
    if re.match(kurs, word):
        for word1 in talabalar[kurs].keys():
            if re.match(andoza, word1):
                print(talabalar[kurs].keys())
                matches[andoza] = talabalar[kurs][word1]
    else:
        print(0)

print(matches)



















# suz = []
# for s in talabalar['2']:
#     suz.append(s.split())
    
    
    # print(s.split())
# kurs = input(".>>>  ")
# andoza = input('>>>  ')
# suz = []
# for a in talabalar['3'].keys():
#     b = a.split()
#     if re.match("^s ^o", b):
#         print(b)
#     suz.append(b)
# suz = []
# suzlar = {}
# kurs = input(".>>>  ")
# andoza = input('>>>  ')
# for a in talabalar[kurs]:
#     word = a.split()
#     suzlar.append(word)
    
    # if re.match('salim olimov', a):
    #     pass
    # if re.match('salim olimov', a):
    #     print(3)
    #     for b in a:
    #         print(b, end="")

# kurs = input(".>>>  ")
# andoza = input('>>>  ')
# matches = {}
# for word in talabalar.keys():
#     if re.match(kurs, word):
#         for word1 in talabalar[kurs].keys():
#             if re.match(andoza, word1):
#                 matches[andoza] = talabalar[kurs][word1]
#     else:
#         print(0)

# print(matches)