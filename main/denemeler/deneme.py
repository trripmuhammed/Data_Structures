import collections

T1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

print(T1[2:14])

array1 = [
    "i",
    [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
    ],
]
liste = [1, 2, 3, 4, 5, 6, 7]

sozluk1 = {"Bir": 1, "Iki": 2}
sozluk2 = {"Uc": 3, "Dort": 4}

CM = collections.ChainMap(sozluk1, sozluk2)

print(list(CM.keys()))
print(list(CM.values()))
print(CM.parents)