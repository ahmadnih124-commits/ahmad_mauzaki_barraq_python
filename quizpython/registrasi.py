
import sqlite3
import os
import textwrap
from datetime import datetime

# ==========================================
# SISTEM REGISTRASI SISWA BARU
# Python + SQLite | Terminal VS Code
# ==========================================

DB_NAME = "database_sekolah.db"

# Warna terminal
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
WHITE = "\033[97m"
MAGENTA = "\033[95m"


def koneksi():
    return sqlite3.connect(DB_NAME)


def siapkan_database():
    with koneksi() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS siswa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nisn TEXT UNIQUE NOT NULL,
                nik TEXT,
                nama TEXT NOT NULL,
                tempat_lahir TEXT,
                tanggal_lahir TEXT,
                jenis_kelamin TEXT,
                agama TEXT,
                alamat TEXT,
                asal_sekolah TEXT,
                kelas TEXT,
                jurusan TEXT,
                nama_ortu TEXT,
                no_hp TEXT,
                tanggal_daftar TEXT NOT NULL
            )
        """)


def garis():
    print(CYAN + "=" * 76 + RESET)


def judul():
    os.system("cls" if os.name == "nt" else "clear")
    garis()
    print(CYAN + BOLD + "          SISTEM INFORMASI REGISTRASI SISWA BARU" + RESET)
    print(WHITE + "                  PENERIMAAN PESERTA DIDIK" + RESET)
    print(YELLOW + "                  Tahun Ajaran 2026/2027" + RESET)
    garis()


def jeda():
    input(f"\n{YELLOW}Tekan ENTER untuk melanjutkan...{RESET}")


def input_wajib(label):
    while True:
        nilai = input(f"{CYAN}{label:<25}{RESET}: ").strip()
        if nilai:
            return nilai
        print(RED + "Data wajib diisi!" + RESET)


def input_opsional(label):
    return input(f"{CYAN}{label:<25}{RESET}: ").strip()


def pilih(label, pilihan):
    print(f"\n{BOLD}{label}{RESET}")
    for i, item in enumerate(pilihan, 1):
        print(f"  {i}. {item}")

    while True:
        nomor = input("Pilih nomor: ").strip()
        if nomor.isdigit() and 1 <= int(nomor) <= len(pilihan):
            return pilihan[int(nomor) - 1]
        print(RED + "Pilihan tidak valid." + RESET)


def registrasi():
    judul()
    print(GREEN + BOLD + "FORMULIR PENDAFTARAN SISWA BARU" + RESET)
    print("Isi data siswa di bawah ini.\n")

    nisn = input_wajib("NISN")
    nik = input_opsional("NIK")
    nama = input_wajib("Nama lengkap")
    tempat = input_opsional("Tempat lahir")
    tanggal = input_opsional("Tanggal lahir (DD-MM-YYYY)")

    if tanggal:
        try:
            datetime.strptime(tanggal, "%d-%m-%Y")
        except ValueError:
            print(RED + "Format tanggal salah. Gunakan DD-MM-YYYY." + RESET)
            jeda()
            return

    jk = pilih("Jenis kelamin", [
        "Laki-laki", "Perempuan"
    ])

    agama = pilih("Agama", [
        "Islam", "Kristen", "Katolik",
        "Hindu", "Buddha", "Konghucu", "Lainnya"
    ])

    alamat = input_wajib("Alamat")
    asal = input_wajib("Asal sekolah")

    kelas = pilih("Kelas tujuan", [
        "X", "XI", "XII"
    ])

    jurusan = pilih("Jurusan", [
        "IPA", "IPS", "Bahasa",
        "Teknik", "RPL", "TKJ", "Akuntansi",
        "Manajemen", "Lainnya"
    ])

    ortu = input_wajib("Nama orang tua")
    hp = input_wajib("Nomor HP orang tua")

    print()
    garis()
    print(BOLD + "KONFIRMASI PENDAFTARAN" + RESET)
    print(f"NISN          : {nisn}")
    print(f"NIK           : {nik or '-'}")
    print(f"Nama          : {nama}")
    print(f"Tempat lahir  : {tempat or '-'}")
    print(f"Tanggal lahir : {tanggal or '-'}")
    print(f"Jenis kelamin : {jk}")
    print(f"Agama         : {agama}")
    print(f"Alamat        : {alamat}")
    print(f"Asal sekolah  : {asal}")
    print(f"Kelas         : {kelas}")
    print(f"Jurusan       : {jurusan}")
    print(f"Orang tua     : {ortu}")
    print(f"No. HP        : {hp}")
    garis()

    konfirmasi = input("Simpan pendaftaran? (Y/T): ").strip().lower()

    if konfirmasi != "y":
        print(YELLOW + "Pendaftaran dibatalkan." + RESET)
        jeda()
        return

    try:
        with koneksi() as conn:
            conn.execute("""
                INSERT INTO siswa (
                    nisn, nik, nama, tempat_lahir, tanggal_lahir,
                    jenis_kelamin, agama, alamat, asal_sekolah,
                    kelas, jurusan, nama_ortu, no_hp, tanggal_daftar
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                nisn, nik, nama, tempat, tanggal, jk, agama,
                alamat, asal, kelas, jurusan, ortu, hp,
                datetime.now().strftime("%d-%m-%Y %H:%M")
            ))

        print(GREEN + BOLD + "\nPENDAFTARAN BERHASIL DISIMPAN!" + RESET)
        print("Nomor registrasi:", nisn)

    except sqlite3.IntegrityError:
        print(RED + "\nGAGAL: NISN sudah terdaftar." + RESET)

    except sqlite3.Error as e:
        print(RED + f"\nTerjadi kesalahan database: {e}" + RESET)

    jeda()


def lihat_siswa():
    judul()
    print(BOLD + "DAFTAR SISWA TERDAFTAR" + RESET + "\n")

    with koneksi() as conn:
        data = conn.execute("""
            SELECT id, nisn, nama, kelas, jurusan, asal_sekolah
            FROM siswa ORDER BY id DESC
        """).fetchall()

    if not data:
        print(YELLOW + "Belum ada data siswa." + RESET)
        jeda()
        return

    print(f"{'ID':<5} {'NISN':<15} {'NAMA':<24} {'KLS':<5} {'JURUSAN':<14} ASAL SEKOLAH")
    garis()

    for row in data:
        id_s, nisn, nama, kelas, jurusan, asal = row
        print(
            f"{id_s:<5} {nisn[:14]:<15} "
            f"{nama[:23]:<24} {kelas:<5} "
            f"{jurusan[:13]:<14} {asal[:25]}"
        )

    garis()
    print(f"Total siswa terdaftar: {len(data)}")
    jeda()


def cari_siswa():
    judul()
    print(BOLD + "PENCARIAN DATA SISWA" + RESET + "\n")
    kata = input_wajib("NISN atau nama")

    with koneksi() as conn:
        data = conn.execute("""
            SELECT id, nisn, nik, nama, tempat_lahir, tanggal_lahir,
                   jenis_kelamin, agama, alamat, asal_sekolah,
                   kelas, jurusan, nama_ortu, no_hp, tanggal_daftar
            FROM siswa
            WHERE nisn LIKE ? OR nama LIKE ?
            ORDER BY nama
        """, (f"%{kata}%", f"%{kata}%")).fetchall()

    if not data:
        print(RED + "\nData siswa tidak ditemukan." + RESET)
        jeda()
        return

    for s in data:
        garis()
        print(f"{BOLD}ID REGISTRASI : {s[0]}{RESET}")
        print(f"NISN          : {s[1]}")
        print(f"NIK           : {s[2] or '-'}")
        print(f"Nama          : {s[3]}")
        print(f"Tempat lahir  : {s[4] or '-'}")
        print(f"Tanggal lahir : {s[5] or '-'}")
        print(f"Jenis kelamin : {s[6] or '-'}")
        print(f"Agama         : {s[7] or '-'}")
        print(f"Alamat        : {s[8] or '-'}")
        print(f"Asal sekolah  : {s[9] or '-'}")
        print(f"Kelas         : {s[10] or '-'}")
        print(f"Jurusan       : {s[11] or '-'}")
        print(f"Nama orang tua: {s[12] or '-'}")
        print(f"No. HP        : {s[13] or '-'}")
        print(f"Tanggal daftar: {s[14]}")

    garis()
    jeda()


def hapus_siswa():
    judul()
    print(RED + BOLD + "HAPUS DATA SISWA" + RESET + "\n")

    nisn = input_wajib("NISN siswa")

    with koneksi() as conn:
        data = conn.execute(
            "SELECT nama FROM siswa WHERE nisn = ?", (nisn,)
        ).fetchone()

        if not data:
            print(RED + "Data siswa tidak ditemukan." + RESET)
            jeda()
            return

        print(f"Nama siswa: {data[0]}")
        konfirmasi = input("Yakin hapus data ini? (Y/T): ").strip().lower()

        if konfirmasi == "y":
            conn.execute("DELETE FROM siswa WHERE nisn = ?", (nisn,))
            print(GREEN + "Data siswa berhasil dihapus." + RESET)
        else:
            print(YELLOW + "Penghapusan dibatalkan." + RESET)

    jeda()


def statistik():
    judul()
    with koneksi() as conn:
        total = conn.execute("SELECT COUNT(*) FROM siswa").fetchone()[0]
        laki = conn.execute(
            "SELECT COUNT(*) FROM siswa WHERE jenis_kelamin='Laki-laki'"
        ).fetchone()[0]
        perempuan = conn.execute(
            "SELECT COUNT(*) FROM siswa WHERE jenis_kelamin='Perempuan'"
        ).fetchone()[0]

        kelas = conn.execute("""
            SELECT kelas, COUNT(*) FROM siswa
            GROUP BY kelas ORDER BY kelas
        """).fetchall()

    print(BOLD + "STATISTIK PENDAFTARAN SISWA" + RESET + "\n")
    print(f"Total siswa       : {total}")
    print(f"Siswa laki-laki   : {laki}")
    print(f"Siswa perempuan   : {perempuan}")
    print("\nJumlah per kelas:")
    if kelas:
        for nama_kelas, jumlah in kelas:
            print(f"  Kelas {nama_kelas:<8}: {jumlah} siswa")
    else:
        print("  Belum ada data.")
    jeda()


def menu():
    siapkan_database()

    while True:
        judul()

        print(f"{GREEN} [1] {WHITE}Registrasi siswa baru{RESET}")
        print(f"{GREEN} [2] {WHITE}Lihat semua siswa{RESET}")
        print(f"{GREEN} [3] {WHITE}Cari detail siswa{RESET}")
        print(f"{GREEN} [4] {WHITE}Statistik pendaftaran{RESET}")
        print(f"{RED}   [5] {WHITE}Hapus data siswa{RESET}")
        print(f"{YELLOW} [0] {WHITE}Keluar dari aplikasi{RESET}")

        garis()
        pilihan = input(f"{BOLD}Pilih menu [0-5]: {RESET}").strip()

        if pilihan == "1":
            registrasi()
        elif pilihan == "2":
            lihat_siswa()
        elif pilihan == "3":
            cari_siswa()
        elif pilihan == "4":
            statistik()
        elif pilihan == "5":
            hapus_siswa()
        elif pilihan == "0":
            print(GREEN + "\nTerima kasih telah menggunakan aplikasi." + RESET)
            break
        else:
            print(RED + "Menu tidak tersedia." + RESET)
            jeda()


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nAplikasi dihentikan.")
