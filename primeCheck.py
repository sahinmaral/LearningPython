# Girilen bir sayinin asal olup oladigini bulun
# Asal sayi 1 ve kendisi haric tam boleni olmayan sayilara denir

primeStatus = True

number = int(input('Sayi giriniz : '))
if(number == 1): primeStatus = False
elif(number == 2): primeStatus = True
else:
    for x in range(2,number):
        if(number % x == 0): 
            primeStatus = False
            break
    

if(primeStatus):
    print('Sayiniz , asal sayidir')
else:
    print('Sayiniz , asal sayi degildir')