from dis import dis
import math


urunA = 5000
urunB = 6000
kdv = 0.2

print(urunA + (urunA * kdv))
print(urunB + (urunB * kdv))

sayi1 = 20
sayi2 = 30
_sayi1 = 20
sayi_1 = 20

print(sayi_1)
print(_sayi1)

a , b , c = 10,20,30
print(a,b,c)

name = 'Sahin'
print(type(name))

isStudent = True
print(type(isStudent))

text1 = '20'
text2 = '30'

print(int(text1)+int(text2))

print(type(str(sayi1)))

radius = 2

print('Yaricapi 2 cm verilen dairenin alani : '+str(math.pi*radius*radius))
print('Yaricapi 2 cm verilen dairenin cevresi : '+str(math.pi*2*radius))

distanceKilometer = 10
print('Verilen kilometre cinsine gore mil hesaplama : '+str(distanceKilometer/1.609344))