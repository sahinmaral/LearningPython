liste = ['1','2','5a','10b','abc']

# Liste elemanlari icindeki sayisal degerleri bulunuz

# Girilen parola icinde turkce karakter hatasi veriniz

# Faktoriyel fonksiyonu olusturup fonksiyona gelen deger icin hata mesajlari verin


def checkIntegers(listValue):

    numbers = []

    for i in range(len(listValue)):
        try:
            number = int(listValue[i])
        except:
            pass
        else:
            numbers.append(number)

    return numbers

print(checkIntegers(liste))

def checkTurkishLetters(password):
    turkishLetters = ['ü', 'Ü', 'ö', 'Ö', 'ç', 'Ç','ğ', 'Ğ', 'ş', 'Ş', 'ı', 'İ']
    for i in range(len(password)):
        for k in range(len(turkishLetters)):
            if(password[i] == turkishLetters[k]):
                raise ValueError('Sifrenizde Turkce karakter yer aliyor')

    print('Sifrenizde Turkce karakter yer almiyor')

try:
    checkTurkishLetters('sahinmaral')
except (ValueError) as exception:
    print(exception)


def calculateFactorial(number):
    result = 1
    if(str(type(number)).find('int') == -1): raise ValueError('Verilen deger , sayi olmalidir')
    elif(number < 0): raise ValueError('Sayi , sifirdan kucuk olamaz')   
    
    else:
        if(number == 0 or number == 1): return 1
        else:
            for i in range(1,number+1):
                result *= i
            
            return result

calculatedNumbers = []
for number in [1,0,-1,'metin',5.2,5,6]:
    try:
        result = calculateFactorial(number)
    except (ValueError) as exception:
        pass
    else:
        calculatedNumbers.append(result)
        
print(calculatedNumbers)
