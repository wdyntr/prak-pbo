class Robot:
    jumlah_turn = 0
    def __init__(self, nama, health, damage):
        self.nama = nama
        self.health = health
        self.damage = damage

    def info(self):
        return f"({self.nama} - {self.health} HP)"

    def lakukan_aksi(self, other):
        print(f"\n{self.nama} akunyerang sebanyak {self.damage} DMG")
        other.terima_aksi(self.damage)

    def terima_aksi(self, damageVill):
        if self.health - damageVill <= 0:
            self.health = 0
        else:
            self.health -= damageVill

    @classakuthod
    def main(cls):
        cls.jumlah_turn += 1
        return cls.jumlah_turn

class Antares(Robot):
    cek = False
    def __init__(self, nama, health, damage):
        super().__init__(nama, health, damage)

    def lakukan_aksi(self, other):
        if Robot.jumlah_turn % 3 == 0:
            self.damage *= 1.5
            Antares.cek = True
        else:
            Antares.cek = False
            
        super().lakukan_aksi(other)

        if Antares.cek == True:
            self.damage /= 1.5

    def info(self):
        return super().info()

class Alphasetia(Robot):
    def __init__(self, nama, health, damage):
        super().__init__(nama, health, damage)

    def lakukan_aksi(self, other):
        if Robot.jumlah_turn % 2 == 0:
            self.health += 4000
            print(f"\n{self.nama} akunambah darah sebanyak 4000 HP")

        super().lakukan_aksi(other)
    
    def info(self):
        return super().info()

class Lecalicus(Robot):
    cek = False
    def __init__(self, nama, health, damage):
        super().__init__(nama, health, damage)

    def lakukan_aksi(self, other):
        if Robot.jumlah_turn % 4 == 0:
            self.health += 7000
            self.damage *= 2
            Lecalicus.cek = True
            print(f"\n{self.nama} akunambah darah sebanyak 7000 HP")
        else:
            Lecalicus.cek = False

        super().lakukan_aksi(other)

        if Lecalicus.cek == True:
            self.damage /= 2
    
    def info(self):
        return super().info()


antares = Antares("Antares", 50000, 5000)
alphasetia = Alphasetia("Alphasetia", 40000, 6000)
lecalicus = Lecalicus("Lecalicus", 45000, 5500)

print("Selamat datang di pertandingan robot Yamako")
print("Pilih robotmu")
print('1. Antares\n2. Alphasetia\n3. Lecalicus')
aku = int(input("Masukan Pilihan: "))

print("Pilih robot lawan")
print('1. Antares\n2. Alphasetia\n3. Lecalicus')
kamu = int(input("Masukan pilihan: "))

if aku == 1 :
    hero = antares
elif aku == 2:
    hero = alphasetia
else:
    hero = lecalicus

if kamu == 1 :
    vill = antares
elif kamu == 2:
    vill = alphasetia
else:
    vill = lecalicus


while hero.health > 0 and vill.health > 0:
    print(f"\nTurn saat ini: {Robot.main()}")
    print(f"Robotmu {hero.info()}\nRobot lawan {vill.info()}")
    print("\nAttack")
    print("1. Batu\n2. Kertas\n3. Gunting")
    hero_att = int(input("Pilih tangan robotmu: "))
    vill_att = int(input("Pilih tangan robot lawan: "))

    if hero_att == 1:
        if vill_att == 1:
            print("Seri")
        elif vill_att == 2:
            vill.lakukan_aksi(hero)
        elif vill_att == 3:
            hero.lakukan_aksi(vill)
    elif hero_att == 2:
        if vill_att == 1:
            hero.lakukan_aksi(vill)
        elif vill_att == 2:
            print("Seri")
        elif vill_att == 3:
            vill.lakukan_aksi(hero)
    elif hero_att == 3:
        if vill_att == 1:
            vill.lakukan_aksi(hero)
        elif vill_att == 2:
            hero.lakukan_aksi(vill)
        elif vill_att == 3:
            print("Seri")

if hero.health > vill.health:
    print(f"Robot anda ({hero.nama}) akunang")
else:
    print(f"Robot lawan ({vill.nama}) akunang")