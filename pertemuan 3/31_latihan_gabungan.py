# Latihan gabungan materi perulangan dan list

list_1 = [10, 70, 20]

print("=== LIST ===")
for i, value in enumerate(list_1):
    print("index:", i, "elem:", value)

print("\n=== RANGE ===")
for i in range(5):
    print("index:", i)

print("\n=== NESTED LIST ===")
matrix = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
]

for row in matrix:
    for cell in row:
        print(cell, end=" ")
    print()

print("\n=== STRING ===")
for char in "hello python":
    print(char)
