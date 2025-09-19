from utils import simpan_ke_file, baca_dari_file

users = {}

def load_users():
    global users
    users = baca_dari_file("users.txt")   

def tambah_user(username, password, role="user"):
    if username in users:
        print("⚠️ Username sudah ada!")
    else:
        users[username] = {"password": password, "role": role}
        print(f"✅ User {username} berhasil ditambahkan!")

def login(username, password):
    if username in users and users[username]["password"] == password:  
        print(f"✅ Login berhasil! Selamat datang, {username}.")
        return users[username]["role"]
    else:
        print("❌ Username atau password salah.")
        return None

def tampilkan_users():
    if not users:
        print("⚠️ Belum ada user.")
        return
    print("\nDaftar User:")
    print("="*40)
    for user, data in users.items():
        print(f"Username: {user} | Role: {data['role']}")   
    print("="*40)

def simpan_users():
    simpan_ke_file(users, "users.txt")  
