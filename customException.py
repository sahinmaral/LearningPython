# x = 10

# if x > 5:
#     raise ValueError('x , besten buyuk olamaz')

def checkPassword(password):
    import re #regular expression
    if(len(password) < 8): raise ValueError('Sifre , sekizden buyuk olmalidir')
    elif(not re.search('[a-z]',password)): raise ValueError('Sifre icerisinde kucuk harf bulunmalidir')
    elif(not re.search('[A-Z]',password)): raise ValueError('Sifre icerisinde buyuk harf bulunmalidir')
    elif(not re.search('[0-9]',password)): raise ValueError('Sifre icerisinde rakam bulunmalidir')
    elif(not re.search('[_@$]',password)): raise ValueError('Sifre icerisinde alfa numerik karakter bulunmalidir')
    elif(re.search('[\s]',password)): raise ValueError('Sifre icerisinde bosluk bulunmamalidir')

password = '123ss24Aa@'

try:
    checkPassword(password)
except (ValueError) as exception:
    print(exception)
else:
    print('Sifreniz onaylandi')
finally:
    print('Sifre dogrulamasi tamamlandi')


