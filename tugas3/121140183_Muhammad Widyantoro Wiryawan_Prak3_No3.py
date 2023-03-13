class Hero:
    def __init__(self, name, power, health):
        # atribut private
        self.__name = name
        # atribut protected
        self._power = power
        # atribut public
        self.health = health
    
    def info(self):
        return f"Hero {self.__name}\nHealth: {self.health}\nPower: {self._power}"
    
    def info_private(self):
        return self.__name

    # fungsi public
    def set_nama(self, nama_baru):
        self.__name = nama_baru

    # fungsi protected
    def _info_protected(self):
        return self._power

    # fungsi public
    def set_power(self, power_baru):
        self._power = power_baru
    
    # fungsi public
    def info_public(self):
        return self.health

# membuat objek
gehrman = Hero("Gehrman", 10, 150)

# menampilkan info
print(gehrman.info())    

# mengakses atribut private dengan fungsi pulic
print(f"Nama Hero: {gehrman.info_private()}")

# mengakses atribut protected dengan fungsi protected
print(f"Power Hero: {gehrman._info_protected()}")

# mengakses atribut public dengan fungsi public
print(f"Health Hero: {gehrman.info_public()}")

# mengubah atribut private menggunakan fungsi public
gehrman.set_nama("Klein")
# menampilkan nama baru
print(f"\nNama Hero: {gehrman.info_private()}")
# karena atribut private tidak dapat diakses langsung diluar class maka perlu fungsi public untuk mengubah nilai atribut private tesebut


# mengubah atribut protected menggunakan fungsi public
gehrman.set_power(15)
# menampilkan Power baru
print(f"Power Hero: {gehrman._info_protected()}")

# mengubah nilai atribut public secara langsung
gehrman.health = 30
print(f"Health Hero: {gehrman.info_public()}")

print("======================================================")
print(gehrman.info())