import random

# 1-100 arasinda rastgele uretilecek bir sayiyi buyk ve kucuk ifadeleri ile buldurmaya 👏 
# random modulunu arstirin
# 100 uzerinden puanlama yapin. Her soru 20 puan

randomNumber = int((random.random() * 100 ) + 1)

countingNumber = 0
remaining = 5
wrongGuess = 0

while(remaining != 0):
    countingNumber = int(input('Sayi giriniz : '))
    if(countingNumber < 0):
        print('Negatif sayilar girilemez')
        remaining -= 1
        wrongGuess += 1
        continue
    if(countingNumber > randomNumber):
        print('Girdiginiz sayi , tahmin edeceginiz sayidan buyuk')
        remaining -= 1
        wrongGuess += 1
    elif(countingNumber < randomNumber):
        print('Girdiginiz sayi , tahmin edeceginiz sayidan kucuk')
        remaining -= 1
        wrongGuess += 1
    else:
        print(f'Tebrikler , dogru bildiniz. Puaniniz {100 - (20)*wrongGuess}')
        break

