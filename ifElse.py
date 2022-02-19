import datetime

# Kullanicidan isim , yas ve egitim bilgilerini isteyip ehliyet alabilme 
# durumunu kontrol ediniz. Ehliyet alma kosulu en az 18 ve egitim durumu 
# lise ya da universite olmalidir

name = input('Isminiz : ')
age = int(input('Yasiniz : '))
education = input('Egitim durumunuz : ')

if(age >= 18 and education == 'lise' or education == 'universite'):
    print('ehliyet alma hakkina sahipsiniz')
else:
    print('ehliyet alma hakkina sahip degilsiniz')

# Bir ogrencinin 2 yazili bir sozlu notunu alip hesaplanan ortalamaya gore 
# not araligina karsilik gelen not bilgisini yazdiriniz
# 0 - 24 => 0
# 25 - 44 => 1
# 45 - 54 => 2
# 55 - 69 => 3
# 70 - 84 => 4
# 85 - 100 => 5

yazili1Not = int(input('Birinci yazili not : '))
yazili2Not = int(input('Ikinci yazili not : '))
sozluNot = int(input('Sozlu not : '))

ortalama = (yazili2Not + yazili1Not + sozluNot) / 3

if(0<=ortalama<=24):
    print('Ders not bilgisi : 0')
elif(25<=ortalama<=44):
    print('Ders not bilgisi : 1')
elif(45<=ortalama<=54):
    print('Ders not bilgisi : 2')
elif(55<=ortalama<=69):
    print('Ders not bilgisi : 3')
elif(70<=ortalama<=84):
    print('Ders not bilgisi : 4')
elif(85<=ortalama<=100):
    print('Ders not bilgisi : 5')


dogumTarihiText = input('Dogum tarihinizi giriniz (gun/ay/yil): ')

dogumTarihiText = dogumTarihiText.split('/')
dogumTarihi = datetime.date(int(dogumTarihiText[2]),int(dogumTarihiText[0]),int(dogumTarihiText[1]))

print(dogumTarihi)