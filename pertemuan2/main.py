# MAIN - Menjalankan latihan dari PDF satu per satu

print("=== PYTHON - LATIHAN DARI PDF ===")
print("Pilih latihan:")
print("1  - print() tanpa string formatting")
print("2  - fungsi id()")
print("3  - membership list")
print("4  - membership tuple")
print("5  - membership dictionary")
print("6  - membership set")
print("7  - membership string")
print("8  - keyword if")
print("9  - block indentation")
print("10 - keyword elif")
print("11 - fungsi input()")
print("12 - type conversion")
print("13 - keyword else")
print("14 - nested condition")
print("15 - operasi logika")
print("16 - one-line & ternary")
print("17 - ternary dengan nilai balik")

pilihan = input("Masukkan nomor latihan: ").strip()

nama_file = {
    "1": "01_print_formatting.py",
    "2": "02_fungsi_id.py",
    "3": "03_membership_list.py",
    "4": "04_membership_tuple.py",
    "5": "05_membership_dictionary.py",
    "6": "06_membership_set.py",
    "7": "07_membership_string.py",
    "8": "08_if.py",
    "9": "09_indentation.py",
    "10": "10_elif_input.py",
    "11": "11_input.py",
    "12": "12_type_conversion.py",
    "13": "13_else.py",
    "14": "14_nested.py",
    "15": "15_logika.py",
    "16": "16_one_line_ternary.py",
    "17": "17_ternary_nilai_balik.py",
}

if pilihan in nama_file:
    with open(nama_file[pilihan], encoding="utf-8") as file:
        kode = file.read()
    exec(kode)
else:
    print("Nomor latihan tidak tersedia.")
