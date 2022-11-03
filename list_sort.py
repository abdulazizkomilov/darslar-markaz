def list_sort(obj_1):
    numbers = []; words = []
    for i in obj_1:
        if type(i) == int:
            numbers.append(i)
        else:
            words.append(i)
    [print(n, end="\n") for n in sorted(numbers)]
    [print(k, end="\n") for k in sorted(words)]


items = ['bahrom', 87, 32, 'husan', 23, 'ali', 'ilhom', 56]
names = [1, 21, 'ali', 43, 'vali', 'rafiq', 10, 'solih', 45, 99]

list_sort(names)
