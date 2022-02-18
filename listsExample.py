# Bmw , Mercedes , Opel , Mazda elemanlarina sahip bir liste olusturunuz
# Liste kac elemanlidir
# Listenin ilk ve son elemani nedir
# Mazda degerini Toyota ile degistiriniz
# Mercedes listenin bir elemani midir
# Listenin -2 indeksindeki deger nedir
# Listenin ilk 3 elemanini alin
# Listenin son 2 elemani yerine Toyota ve Renault degerlerini ekleyin
# Listenin uzerinde Audi ve Nissan degerlerini ekleyin
# Listenin son elemanini silin
# Liste elemanlarini tersten yazdiriniz

carBrands = ['Bmw','Mercedes','Opel','Mazda']
print(len(carBrands))

print(carBrands[0],carBrands[len(carBrands)-1])

carBrands[len(carBrands)-1] = 'Toyota'
print(carBrands)

print(carBrands.__contains__('Mercedes'))

print(carBrands[-2])

print(carBrands[:3])

carBrands[-2:] = ['Toyota','Renault']
print(carBrands)

carBrands.append(['Audi','Nissan'])
print(carBrands)

carBrands.pop()
print(carBrands)

print(carBrands[::-1])\


print('\n')

# Asagidaki verileri bir liste icinde saklayiniz
# studentA : Yigit Bilgi 2010 , (70,60,70)
# studentB : Sena Turan 1999 , (80,80,70)
# studentC : Ahmet Turan 1998 , (80,70,90)

studentA = ['Yigit','Bilgi',2010 , [70,60,70]]
studentB = ['Sena','Turan',1999 , [80,80,70]]
studentC = ['Ahmet','Turan',1998 , [80,70,90]]

print(f'Ogrenci A ismi {studentA[0]} , soyismi {studentA[1]} , dogum tarihi {studentA[2]}')
print(f'Ogrenci A ders notlari 1: {studentA[3][0]} , 2: {studentA[3][1]} , 3: {studentA[3][2]}')

print('\n')

print(f'Ogrenci B ismi {studentB[0]} , soyismi {studentB[1]} , dogum tarihi {studentB[2]}')
print(f'Ogrenci B ders notlari 1: {studentB[3][0]} , 2: {studentB[3][1]} , 3: {studentB[3][2]}')

print('\n')

print(f'Ogrenci C ismi {studentC[0]} , soyismi {studentC[1]} , dogum tarihi {studentC[2]}')
print(f'Ogrenci C ders notlari 1: {studentC[3][0]} , 2: {studentC[3][1]} , 3: {studentC[3][2]}')

