# A.12.4 Fungsi list() - konversi range ke list

range_1 = range(0, 10)
list_1 = list(range_1)
print(list_1)
# output -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

range_2 = range(0, 22, 3)
list_2 = list(range_2)
print(list_2)
# output -> [0, 3, 6, 9, 12, 15, 18, 21]
