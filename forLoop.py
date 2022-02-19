numbers = [1,2,3,4,5]

for number in numbers:
    print(number)
    

d = {'k1':1,'k2':2,'k3':3}

for key,value in d.items():
    print(key,value)

sayilar = [1,3,5,7,9,12,19,21]

# Sayilar listesindeki hangi sayilar 3'un katidir
# Sayilar listesinde sayilarin toplami kactir
# Sayilar listesindeki tek sayilarin karesini aliniz

sumSayilar = 0
oddNumbers = []
squareOddNumbers = []

for number in sayilar:
    if(number % 3): oddNumbers.append(number)
    if(number % 2 == 1): squareOddNumbers.append((number**2))
    sumSayilar += number

print(sumSayilar)
print(oddNumbers)
print(squareOddNumbers)

sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# Sehirlerden hangileri en fazla 5 karakterli olanlari getiriniz

countriesLengthMoreThanFive = []

for country in sehirler:
    if(len(country)<=5): countriesLengthMoreThanFive.append(country)

print(countriesLengthMoreThanFive)

# Urunlerin fiyatlari toplami nedir
# Urunlerden fiyati en fazla 5000 olan urunleri gosteriniz

urunler = [
    {'name':'samsung s6','price':'3000'},
    {'name':'samsung s7','price':'4000'},
    {'name':'samsung s8','price':'5000'},
    {'name':'samsung s9','price':'6000'},
    {'name':'samsung s10','price':'7000'}
]

sumOfProductsPrice = 0
productsPriceMoreThan5000 = []

for product in urunler:
    if(int(product['price']) <= 5000):
        productsPriceMoreThan5000.append(product)
    
sumOfProductsPrice += int(product['price'])

print(sumOfProductsPrice)
print(productsPriceMoreThan5000)