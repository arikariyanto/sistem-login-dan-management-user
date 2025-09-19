from user_manager import *

load_users()   

print("="*50)
print("      SISTEM LOGIN & MANAJEMEN USER     ")
print("="*50)

while True:
    print("\nMenu:")
    print("1. Tambah User")
    print("2. Login")
    print("3. Lihat Semua User")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        username = input("Masukkan username baru: ")
        password = input("Masukkan password: ")
        role = input("Masukkan role (admin/user): ")
        tambah_user(username, password, role)  

    elif pilihan == "2":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        role = login(username, password)  

        if role == "admin":
            print("\n🔑 Menu Admin:")
            print("1. Lihat semua user")
            print("2. Tambah user baru")
            print("3. Logout")

            admin_pilihan = input("Pilih: ")
            if admin_pilihan == "1":
                tampilkan_users()
            elif admin_pilihan == "2":
                u = input("Masukkan username: ")
                p = input("Masukkan password: ")
                r = input("Masukkan role (admin/user): ")
                tambah_user(u, p, r)
            else:
                print("Logout...")

    elif pilihan == "3":
        tampilkan_users()

    elif pilihan == "4":
        simpan_users()  
        print("👋 Keluar dari program. Data tersimpan.")
        break

    else:
        print("⚠️ Pilihan tidak valid!")
