def printText(name = 'user'):
    '''
    DOCSTRING : 'Hello , {name}' yazisi yazar. Name parametresi almazsa user dondurur.
    '''
    print(f'Hello , {name}')

printText('Sahin')

def squareNumber(number):
    return (number ** 2)

print(squareNumber(2))

help(printText)


# Fonksiyon uzerinde atanan deger degisir cunku listeler , referans tiplidir
# Ayni olay string gibi deger tiplerde gecerli degildir
def change(n):
    n[0] = 'istanbul'

sehirler = ['ankara','izmir']
change(sehirler)
print(sehirler)

def sumNumbers(*params):
    sum = 0
    for number in params:
        sum += number
    return sum

print(sumNumbers(10,20,30,6,4))

def displayUser(**args):
    for key,value in args.items():
        print(f'{key} : {value}')

displayUser(name='Sahin',surname='MARAL',age=22)