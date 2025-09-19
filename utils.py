
def simpan_ke_file(data, filename):
    with open(filename, "w") as f:
        for user, info in data.items():
            f.write(f"{user},{info['password']},{info['role']}\n")  

def baca_dari_file(filename):
    data = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                username, password, role = line.strip().split(",")
                data[username] = {"password": password, "role": role}   
    except FileNotFoundError:
        pass
    return data
