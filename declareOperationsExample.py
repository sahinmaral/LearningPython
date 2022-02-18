x,y,z = 2,5,107

numbers = 1,5,7,10,6

# Kullanicidan aldiginiz 2 sayinin carpimi ile x,y,z toplaminin farki nedir
numberExample1 = int(input('numberExample1 : '))
numberExample2 = int(input('numberExample2 : '))

sumTopNumbers = x+y+z
print((numberExample1*numberExample2)-sumTopNumbers)

# y nin x e kalansiz bolumunu hesaplayiniz
print(y//x)

# (x,y,z) toplaminin mod 3'u nedir
print(sumTopNumbers%3)

# y nin x kuvvetini hesaplayiniz
print(y**x)

# x , *y , z = numbers islemine gore z' nin kupu kactir
x , *y , z = numbers
print(z**3)

# x, *y , z = numbers islemine gore y nin degerleri toplami kactir
x, *y , z = numbers

sumYNumbers = 0

for number in y:
    sumYNumbers += number

print(sumYNumbers)