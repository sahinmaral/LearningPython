# import math as mathLibrary
from math import factorial,sqrt,pi
import random

# Bir modulu import ederken yazdigimiz fonksiyonlarin 
# ismiyle kesismemesi gerekir
def sqrt(x):
    print(f'x : {str(x)}')

# print(mathLibrary.pi)
# print(dir(mathLibrary))
# print(help(math))

print(factorial(5))
print(pi)
print(sqrt(3))
print(int(random.random()*3)+1)

# [1, 10) veya [1, 10] araliginda sayi verir , sebebi sayiyi yuvarladigindan dolayidir
print(int(random.uniform(1,10))) 


names = ['Ali','Mehmet','Hasan','Kazim']
# [0, dizi-araligi] araliginda sayi verir , herhangi bir yuvarlama olmadigi icin 
# araliklarin basi ve sonu dahildir
result = names[random.randint(0,len(names)-1)]

# Bos olmamasi gereken liste icerisinden rastgele bir eleman dondurur
result2 = random.choice(names)

print(result)
print(result2)

numberList = list(range(10))

# Liste icerisindeki elemanlarin yerlerini rastgele degistirir
random.shuffle(numberList)
print(numberList)

# Istedigimiz sayi kadar liste icerisinden rastgele sayilar alir
randomThreeNumbers = random.sample(numberList,3)
print(randomThreeNumbers)