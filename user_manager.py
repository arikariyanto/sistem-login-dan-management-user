
from utils import simpan_ke_file, baca_dari_file, simpan_histori

users = {}

def load_users():
    global users
    users = baca_dari_file("users.txt")

def tambah_user(username, password, role):
    users[username] = {"password": password, "role": role}
    simpan_histori(username, "Ditambahkan ke sistem")

def login(username, password):
    if username in users and users[username]["password"] == password:
        simpan_histori(username, "Login berhasil")
        return users[username]["role"]
    else:
        return None

def tampilkan_users():
    for u, info in users.items():
        print(f"{u} - Role: {info['role']}")

def ubah_password(username, new_password):
    users[username]["password"] = new_password
    simpan_histori(username, "Password diubah")

def hapus_user(username):
    if username in users:
        del users[username]
        simpan_histori(username, "User dihapus")

def simpan_users():
    simpan_ke_file(users, "users.txt")
