class AkunBank:
    list_pelanggan = []

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        AkunBank.list_pelanggan.append(self)

    def lihat_menu(self):
        print("Selamat datang di Bank Jago")
        cek = 1
        while cek != 4:
            print(f"Selamat datang {self.__nama_pelanggan}, apa yang ingin anda lakukan?")
            print("1. Lihat saldo")
            print("2. Tarik tunai")
            print("3. Transfer saldo")
            print("4. Keluar")

            cek = int(input("Masukan nomor input: "))
            if cek == 1:
                self.lihat_saldo()
            elif cek == 2:
                self.tarik_tunai()
            elif cek == 3:
                self.transfer()
            print()

    def lihat_saldo(self):
        print(f"{self.__nama_pelanggan} memiliki saldo Rp {self.__jumlah_saldo}")
    
    def tarik_tunai(self):
        nominal = int(input("Masukan jumlah nominal yang ingin ditarik: "))
        if nominal < self.__jumlah_saldo:
            print("Saldo berhasil ditarik")
            self.__jumlah_saldo -= nominal
        else:
            print("Nominal saldo yang anda punya tidak cukup!")

    def transfer(self):
        nominal = int(input("Masukan nominal yang ingin ditransfer: "))
        if nominal < self.__jumlah_saldo:
            rek = int(input("Masukan no rekening tujuan : "))

            rek_tujuan = None
            for rekening in AkunBank.list_pelanggan:
                if rek == rekening.__no_pelanggan:
                    rek_tujuan = rekening
                    break
            
            if rek_tujuan == None:
                print("No rekening tujuan tidak ditemukan! Kembali ke menu utama")
                print()
                self.lihat_menu()
            else:
                self.__jumlah_saldo -= nominal
                rek_tujuan.__jumlah_saldo += nominal
                print(f"Transfer Rp {nominal} ke {rek_tujuan.__nama_pelanggan} berhasil!")


Akun1 = AkunBank(1234, "Widyantoro", 5000000000)
Akun2 = AkunBank(2345, "Gehrman", 6666666666)
Akun3 = AkunBank(3456, "Ucup", 9999999999)

Akun1.lihat_menu()