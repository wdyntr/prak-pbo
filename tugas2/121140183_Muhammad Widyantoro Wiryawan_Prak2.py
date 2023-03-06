class data:

    def __init__(self, nama, alamat, nim, tgl):
        self.nama = nama
        self.alamat = alamat
        self.nim = nim
        self.tgl_lahir = tgl

    def info(self):
        return f"Nama: {self.nama}\nNIM: {self.nim}\nAlamat: {self.alamat}\nTanggal lahir: {self.tgl_lahir}"

nama = input("Masukan nama: ")
nim = input("Masukan NIM: ")
alamat = input("Masukan alamat: ")
tgl = input("Masukan tanggal lahir: ")

data_diri = data(nama, alamat, nim, tgl)
print(data_diri.info())