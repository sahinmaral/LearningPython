sayilar = [1,3,5,7,9,12,19,21]

# sayilar listesini while ile ekrana yazdirin

count = 0

while count != len(sayilar):
    print(sayilar[count])
    count += 1

whileStartPoint = int(input('Hangi sayidan baslamak istersiniz : '))
whileEndPoint = int(input('Hangi sayida bitirmek istersiniz : '))

while whileStartPoint != whileEndPoint:
    if(whileStartPoint % 2 == 1): print(whileStartPoint)
    whileStartPoint += 1

count = 100

while count != 1:
    print(count)
    count -= 1

texts = []

count = 5
while count != 0:
    texts.append(input('Metin giriniz : '))
    count -= 1

for text in texts:
    print(text)

products = []
productCount = int(input('Kac tane urun eklemek istiyorsunuz : '))

while productCount != 0:
    productName = input('Urun adi : ')
    productPrice = input('Urun fiyati : ')
    products.append({'name':productName  , 'price' : productPrice})
    productCount -= 1

for product in products:
    print(product)

# Baslangic ve bitis degerlerini kullanicidan alip aradaki tum tek sayilari ekrana yazdirin
# 1-100 arasindaki sayilari azalan sekilde yazdirin
# Kullanicidan alacaginiz 5 sayiyi ekranda sirali bir sekilde yazdirin
# Kullanicidan alacaginiz sinirsiz urun bilgisini urunler listesi icinde saklanacak
#     Urun sayisini kullaniciya sorun
#     Dictionary listesi yapisi (name,price) seklinde olsun
#     Urun ekleme islemi bittiginde urunleri ekranda while ile listeleyin