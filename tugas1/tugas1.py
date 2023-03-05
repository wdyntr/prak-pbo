import random
angka_pikiran = random.randint(1, 100)

coba = 7
berhasil = False

for i in range(coba):
  print('Anda memiliki ' + str(coba) + ' kesempatan')
  cek = int(input('Tebak angka antara 1 hingga 100 : '))
  if cek != angka_pikiran and cek < angka_pikiran :
    print("Ángka yang anda tebak terlalu kecil")
    coba -= 1
    berhasil = False
  elif cek != angka_pikiran and cek > angka_pikiran:
    print("Angka yang anda tebak terlalu besar")
    coba -= 1
    berhasil = False
  elif cek == angka_pikiran :
    print("Tebakan anda benar")
    berhasil = True
    exit()
  
  print("\n")
    
if berhasil == False:
  print("Ända tidak berhasil menebak angka yang dipikrkan andi. Angka yang benar adalah " + str(angka_pikiran))
elif berhasil == True:
  print("Anda berhasil menebak angka yang dipikirkan andi")
  