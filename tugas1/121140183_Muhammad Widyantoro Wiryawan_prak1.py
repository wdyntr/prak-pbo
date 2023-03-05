print("======================== Latihan 1 ========================")
n = int(input("Masukan angka n: "))

for i in range(n):
    for j in range(n):
        print("*",end="")
    print()

print("\n")
print("======================== Latihan 2 ========================")
username = "informatika"
password = 12345678

ulang = False
i = 1
while not ulang and i <= 3:
    user = input("Username anda: ")
    cek = int(input("Password anda: "))

    if user == username and cek == password:
        print("Berhasil login!")
        ulang = True
    else:
        if i == 3:
            print("Akun anda diblokir")
            break
        else :
            print("Username atau password salah coba lagi")
            ulang = False
            i += 1