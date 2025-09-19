
from user_manager import load_users, tambah_user, login, tampilkan_users, simpan_users, ubah_password, hapus_user

load_users()

while True:
    print("\n=== MENU UTAMA ===")
    print("1. Tambah User")
    print("2. Login")
    print("3. Lihat Semua User")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan username: ")
        pw = input("Masukkan password: ")
        role = input("Masukkan role (admin/editor/viewer): ")
        tambah_user(nama, pw, role)

    elif pilihan == "2":
        nama = input("Masukkan username: ")
        pw = input("Masukkan password: ")
        role = login(nama, pw)
        if role:
            print(f"Login berhasil sebagai {role}")
            if role == "admin":
                while True:
                    print("\n--- MENU ADMIN ---")
                    print("1. Lihat semua user")
                    print("2. Ubah password user")
                    print("3. Hapus user")
                    print("4. Kembali")

                    pilih_admin = input("Pilih: ")
                    if pilih_admin == "1":
                        tampilkan_users()
                    elif pilih_admin == "2":
                        uname = input("Masukkan username: ")
                        new_pw = input("Masukkan password baru: ")
                        ubah_password(uname, new_pw)
                    elif pilih_admin == "3":
                        uname = input("Masukkan username: ")
                        hapus_user(uname)
                    elif pilih_admin == "4":
                        break
        else:
            print("Login gagal!")

    elif pilihan == "3":
        tampilkan_users()

    elif pilihan == "4":
        simpan_users()
        print("Keluar program...")
        break
