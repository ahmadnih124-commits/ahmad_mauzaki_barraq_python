# Halaman 12 - A.8.6 Seleksi kondisi sebaris & ternary

# Bentuk awal:
if grade >= 65:
    print("passed the exam")
else:
    print("below the passing grade")

# One-line / sebaris:
if grade >= 65: print("passed the exam")
if grade < 65: print("below the passing grade")

# Ternary:
print("passed the exam") if grade >= 65 else print("below the passing grade")
