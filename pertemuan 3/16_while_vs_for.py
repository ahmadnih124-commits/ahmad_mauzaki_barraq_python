# A.10.2 Perulangan while vs for
# Versi while
n = int(input("enter max data (while): "))
i = 0

while i < n:
    print("number", i)
    i += 1

# Versi for
n = int(input("enter max data (for): "))

for i in range(n):
    print("number", i)
