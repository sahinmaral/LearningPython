# Gonderilen bir kelimeyi , belirtilen kez ekranda gosteren fonksiyonu yaziniz
# Kendine gonderilen sinirsiz sayidaki parametreyi , listeye ceviren fonksiyon yaziniz
# Gonderilen 2 sayi arasindaki tum asal sayilari bulan fonksiyon yaziniz
# Kendisine gonderilen bir sayinin , tam bolenlerini bir liste seklinde donduren fonksiyon yaziniz

def printText(times,text):
    while(times != 0):
        print(text)
        times -= 1

printText(3,'hello')

def convertList(*params):
    exampleList = []

    for param in params:
        exampleList.append(param)

    return exampleList

print(convertList(10,20,30,40,50))

def primeNumberCheck(number):
    counter = 2

    if(number == 1): return False
    elif(number == 2): return False
    else:
        while counter != number:
            if(number % counter == 0):
                return False
            counter += 1

        return True
    

def findPrimeNumberBetweenTwoNumbers(number1,number2):

    primeNumbers = []

    while(number1 != number2):
        if(primeNumberCheck(number1)):
            primeNumbers.append(number1)
        number1 += 1

    return primeNumbers

print(findPrimeNumberBetweenTwoNumbers(17,30))

def findCommonDividersOfNumber(number):
    commonDividers = []
    count = 1
    while(count != number):
        if(number % count == 0 and count != 1):
            commonDividers.append(count)
        count += 1

    return commonDividers

print(findCommonDividersOfNumber(30))
