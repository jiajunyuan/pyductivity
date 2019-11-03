dict_1 = {'a': [1, 'x'], 'b': [2, 'y'], 'c': [3, 'z']}
dict_2 = {'ace': ['a', 1], 'base': ['b', 2], 'cace': ['c', 3], }
dict_3 = {}

for x in dict_2:
    dict_3[x] = dict_2[x]

print(dict_3)
