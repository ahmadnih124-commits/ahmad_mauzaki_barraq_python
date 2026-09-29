# PERTEMUAN 3 - PYTHON TUPLE
# Berdasarkan materi PDF

# 1. Membuat tuple
tuple_1 = (2, 3, 4, "hello python", False)
print("1. Tuple:", tuple_1)
print("Jumlah element:", len(tuple_1))

# 2. Mengakses tuple via index
tuple_1 = (2, 3, 4, 5)
print("\n2. Akses index:")
print("elem 0:", tuple_1[0])
print("elem 1:", tuple_1[1])

# 3. Perulangan tuple
tuple_2 = ('ultra instinc shaggy', 'nightwing', 'noob saibot')
print("\n3. Perulangan:")
for t in tuple_2:
    print(t)

# 4. Perulangan dengan index
print("\n4. Perulangan dengan index:")
for i in range(0, len(tuple_2)):
    print("index:", i, "elem:", tuple_2[i])

# 5. enumerate()
print("\n5. Enumerate:")
for i, v in enumerate(tuple_2):
    print("index:", i, "elem:", v)

# 6. Mengecek element
tuple_1 = (10, 70, 20)
n = 70
print("\n6. Cek element:")
if n in tuple_1:
    print(n, "is exists")
else:
    print(n, "is NOT exists")

# 7. Nested tuple
tuple_nested = ((0, 2), (0, 3), (2, 2), (2, 4))
print("\n7. Nested tuple:")
for row in tuple_nested:
    for cell in row:
        print(cell, end=" ")
    print()

# 8. List berisi tuple
data = [
    ("ultra instinc shaggy", 1, True, ['detective', 'saiyan']),
    ("nightwing", 3, True, ['teen titans', 'bat family']),
]

data.append(("noob saibot", 6, False, ['brotherhood of shadow']))
data.append(("tifa lockhart", 2, True, ['avalanche']))

print("\n8. List berisi tuple:")
print("name | rank | win | affiliation")
print("------------------------------")
for row in data:
    for cell in row:
        print(cell, end=" | ")
    print()

# 9. Konversi string ke tuple
alphabets = tuple('abcdefgh')
print("\n9. String ke tuple:")
print(alphabets)

# 10. Konversi list ke tuple
numbers = tuple([2, 3, 4, 5])
print("\n10. List ke tuple:")
print(numbers)

# 11. Konversi range ke tuple
r = range(0, 3)
rtuple = tuple(r)
print("\n11. Range ke tuple:")
print(rtuple)

# 12. Tuple packing
first_name = "aerith gainsborough"
rank = 11
win = False
row_data = (first_name, rank, win)
print("\n12. Tuple packing:")
print(row_data)

# 13. Tuple unpacking
row_data = ('aerith gainsborough', 11, False)
first_name, rank, win = row_data
print("\n13. Tuple unpacking:")
print(first_name, rank, win)

# 14. Tuple kosong
empty_tuple = ()
print("\n14. Tuple kosong:")
print(empty_tuple)

# 15. Data akhir sesuai contoh materi
data = [
    ("ultra instinc shaggy", 1, True, ('detective', 'saiyan')),
    ("nightwing", 3, True, ('teen titans', 'bat family')),
    ("kucing meong", 7, False, ()),
]

print("\n15. Data tuple lengkap:")
for row in data:
    print(row)
