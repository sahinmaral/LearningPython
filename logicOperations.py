x = 5
result = 5 < x < 10
result2 = x > 5 and x < 10
result3 = not (x > 5 or x > 0)

# Girilen bir sayinin 0-100 arasinda olup olmadigini kontrol ediniz
# Girilen bir sayinin pozitif cift sayi olup olmadigini kontrol ediniz
# Email ve parola bilgileri ile giris kontrolu yapiniz
# Girilen 3 sayiyi buyukluk olarak karsilastiriniz
# Kullanicidan 2 vize (%60) ve final (%40) notunu alip ortalama hesaplayiniz
# Eger ortalama 50 ve ustudeyse gecti , degilse kaldi yazdirin
# Ortalama 50 olsa bile final notu en az 50 olmalidir
# Finalden 70 alindiginda ortalamanin onemi olmasin

# Kisinin ad, kilo ve boy bilgilerini alip kilo indeksini hesaplayiniz
# Formul = (kilo/ (boy**2))

# Asagidaki tabloya gore kisi hangi gruba girmektedir
# 0-18.4 Zayif
# 18.5-24.9 Normal
# 25.0 - 29.9 Fazla kilolu
# 30.0 - 34.9 Sisman(Obez)

number1 = int(input("Number to check between 0 to 100 : "))

if 0 < number1 < 100:
    print("Sayi 0 ile 100 arasinda")
else:
    print("Sayi 0 ile 100 arasinda degil")

number2 = int(input("Number to check positive even number : "))
if number2 % 2 == 0 and number2 > 0:
    print("Sayi , pozitif cift sayi")
else:
    print("Sayi , pozitif cift sayi degil")

email = "sahin.maral@hotmail.com"
parola = "123"

emailCheck = input("Email : ")
parolaCheck = input("Parola : ")

if emailCheck == email and parola == parolaCheck:
    print("Dogru giris")
else:
    print("Hatali giris")


compareNumber1 = input("Number 1 : ")
compareNumber2 = input("Number 2 : ")
compareNumber3 = input("Number 3 : ")

if compareNumber1 > compareNumber2 and compareNumber1 > compareNumber3:
    if compareNumber2 > compareNumber3:
        print("Buyukten kucuge : birinci - ikinci - ucuncu")
    else:
        print("Buyukten kucuge : birinci - ucuncu - ikinci")
elif compareNumber2 > compareNumber1 and compareNumber2 > compareNumber3:
    if compareNumber1 > compareNumber3:
        print("Buyukten kucuge : ikinci - birinci - ucuncu")
    else:
        print("Buyukten kucuge : ikinci - ucuncu - compareNumber1")
elif compareNumber3 > compareNumber1 and compareNumber3 > compareNumber2:
    if compareNumber1 > compareNumber2:
        print("Buyukten kucuge : ucuncu - birinci - ikinci")
    else:
        print("Buyukten kucuge : ucuncu - ikinci - birinci")

vize1Not = float(input('Vize 1 Not : '))
vize2Not = float(input('Vize 2 Not : '))
finalNot = float(input('Final Not : '))

ortalama = (((vize1Not+vize2Not)*0.6) + (finalNot * 0.4))

if(finalNot > 70):
    print('gecti')
elif(ortalama >= 50):
    if(finalNot < 50):
        print('kaldin')
    else:
        print('gectin')
else:
    print('kaldin')

ad = input('Adiniz : ')
kilo = int(input('Kilonuz : '))
boy = int(input('Boyunuz : '))

bms = kilo/ ((boy*(10**-2))**2)
result = ''

if(0<bms<18.4):
    result = 'Zayif'
elif(18.5<bms<24.9):
    result = 'Normal'
elif(18.5<bms<24.9):
    result = 'Fazla kilolu'
else:
    result = 'Sisman(Obez)'

print(f'{ad} isimli kisinin vucut kutle indeksi {bms} olmus olup {result} kategorisindedir')