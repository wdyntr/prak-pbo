from abc import ABC, abstractmethod

class AkunBank(ABC):
    
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo
        
    def lihat_saldo(self):
        return f"\nSaldo saat ini adalah {self.saldo:,}"
    
    @abstractmethod
    def transfer_saldo(self):
        pass
    
    @abstractmethod
    def lihat_suku_bunga(self):
        pass
    
class AkunGold(AkunBank):
    lama = 0
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)
        
    def transfer_saldo(self):
        AkunGold.lama = 2023 - self.tahun_daftar
        n = int(input("Masukan jumlah transfer: "))
        if AkunGold.lama >= 3 and n > 100000:
            self.saldo -= n
            print("Anda terbebas biaya admin")
            print("Transfer anda berhasil")
        elif AkunGold.lama < 3 and n > 100000:
            n += 2000
            self.saldo -= n
            print('Anda terkena biaya admin sebesar 2000')
            print("Transfer anda berhasil")
        else:
            self.saldo -= n
            print("Anda terbebas biaya admin")
            print("Transfer anda berhasil")        
            
    def lihat_suku_bunga(self):
        print('\nInformasi anda:')
        print(f'Nama: {self.nama}\nTahun daftar: {self.tahun_daftar}\nSaldo anda: {self.saldo:,}')
        print('-' * 20)
        print("Informasi suku bunga")
        print('-' * 20)

        AkunGold.lama = 2023 - self.tahun_daftar
        if AkunGold.lama >= 3 and self.saldo >= 1000000000:
            bunga = (self.saldo * 0.01 * 29) / 365
            self.saldo += bunga
            print(f"Bunga anda sebesar 1% dengan jumlah {bunga:,} {self.lihat_saldo()}")
        elif AkunGold.lama < 3 and self.saldo >= 1000000000:
            bunga = (self.saldo * 0.02 * 29) / 365
            self.saldo += bunga
            print(f"Bunga anda sebesar 2% dengan jumlah {bunga:,} {self.lihat_saldo()}")
        else:
            bunga = (self.saldo * 0.03 * 29) / 365
            self.saldo += bunga
            print(f"Bunga anda sebesar 3% dengan jumlah {bunga:,} {self.lihat_saldo()}")
            
    def lihat_saldo(self):
        return super().lihat_saldo()

class AkunSilver(AkunBank):
    lama = 0
    def __init__(self, nama, tahun_daftar, saldo):
        super().__init__(nama, tahun_daftar, saldo)

    def transfer_saldo(self):
        AkunSilver.lama = 2023 - self.tahun_daftar
        n = int(input("Masukan jumlah transfer: "))
        if AkunSilver.lama >= 3 and n > 100000:
            n += 2000
            self.saldo -= n
            print('Anda terkena biaya admin sebesar 2000')
        elif AkunSilver.lama < 3 and n > 100000:
            n += 5000
            self.saldo -= n
            print('Anda terkena biaya admin sebesar 5000')
            print("Transfer anda berhasil")
        else:
            self.saldo -= n
            print("Anda terbebas biaya admin")
            print("Transfer anda berhasil")

    def lihat_suku_bunga(self):
        print('\nInformasi anda:')
        print(f'Nama: {self.nama}\nTahun daftar: {self.tahun_daftar}\nSaldo anda: {self.saldo:,}')
        print('-' * 20)
        print("Informasi suku bunga")
        print('-' * 20)

        AkunSilver.lama = 2023 - self.tahun_daftar
        if AkunSilver.lama >= 3 and self.saldo >= 10000000:
            bunga = (self.saldo * 0.01 * 29) / 365
            self.saldo += bunga
            print(f"Bunga anda sebesar 1% dengan jumlah {bunga:,} {self.lihat_saldo()}")
        elif AkunSilver.lama < 3 and self.saldo >= 10000000:
            bunga = (self.saldo * 0.02 * 29) / 365
            self.saldo += bunga
            print(f"Bunga anda sebesar 2% dengan jumlah {bunga:,} {self.lihat_saldo()}")
        else:
            bunga = (self.saldo * 0.03 * 29) / 365
            self.saldo += bunga
            print(f"Bunga anda sebesar 3% dengan jumlah {bunga:,} {self.lihat_saldo()}")

    def lihat_saldo(self):
        return super().lihat_saldo()


nama = input("Masukan nama anda: ")
tahun = int(input("Masukan tahun daftar: "))
saldo = int(input("Masukan saldo anda: "))
akun = int(input("1. Akun Gold\n2. Akun Silver\nMasukan akun anda: "))

if akun == 1:
    print('-'* 15, 'Akun Gold', '-'* 15)
    aku = AkunGold(nama, tahun, saldo)
    aku.transfer_saldo()
    print(aku.lihat_saldo())
    aku.lihat_suku_bunga()
else :
    print('-'* 15, 'Akun Silver', '-'* 15)
    kamu = AkunSilver(nama, tahun, saldo)
    kamu.transfer_saldo()
    print(kamu.lihat_saldo())
    kamu.lihat_suku_bunga()
