print(True == 1)

# Girilen 2 sayidan hangisi buyuktur ?
# Kullanicidan 2 vize (%60) ve final (%40) notunu alip ortalama hesaplayiniz
# Eger ortalama 50 ve ustudeyse gecti , degilse kaldi yazdirin

# Girilen bir sayinin tek mi cift mi oldugunu yazdirin
# Girilen bir sayinin negatif pozitif durumunu yazdirin

# Parola ve email bilgisini isteyip dogrulugunu kontrol ediniz
# (email : sahin.maral@hotmail.com , parola : 12345)

firstNumber = input('First Number : ')
secondNumber = input('Second Number : ')

if(firstNumber > secondNumber):
    print('Ilk sayi , ikincisinden buyuk')
elif(secondNumber > firstNumber):
    print('Ikinci sayi , ilkinden buyuk')
else:
    print('Sayilar , birbirine esit')

vize1Not = float(input('Vize 1 Not: '))
vize2Not = float(input('Vize 2 Not: '))
finalNot = float(input('Final Not: '))

ortalamaNot = ((vize1Not+vize2Not) * 0.6) + (finalNot * 0.4)

if(ortalamaNot >= 50):
    print('gecti')
else:
    print('kaldi')

evenOddNumberCheck = int(input('Number to check if number is even or odd : '))

print('Sayi cift') if evenOddNumberCheck % 2 == 0 else print('Sayi tek')

negativePositiveNumberCheck = int(input('Number to check if number is negative or positive : '))

print('Sayi pozitif') if negativePositiveNumberCheck > 0 else print('Sayi negatif')