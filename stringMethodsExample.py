website = 'https://www.sadikturan.com'
course = 'Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)'

# ' Hello World ' karakter dizisinin bas ve sondaki bosluk karakterlerini silin
text = ' Hello World '
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# www.sadikturan.com icindeki sadikturan bilgisi haricindeki her karakteri silin
text2 = website.replace('www.','').replace('.com','')
print(text2)

# course karakter dizisinin tum karakterlerini kucuk harf yapin
print(course.lower())

# website icinde kac tane a karakteri vardir ?
print(website.count('a'))

# website www ile baslayip com ile bitiyor mu ?
isWebsiteCorrect = website.startswith('https://www') & website.endswith('com')
print(isWebsiteCorrect)

# website icinde .com ifadesi var mi
isIncludedDomain = website.find('.com') != -1
print(isIncludedDomain)

# course icindeki karakterlerin hepsi alfabetik mi
print(course.isalpha()) # Alfabetik kontrol
print(course.isdigit()) # Sayi kontrol

# Contens ifadesini satirda 50 karakter icine yerlestirip sag ve soluna * ekleyiniz
print('Contents'.center(50,'*'))

# course karakter dizisindeki tum bosluk karakterlerini '-' ile degistirin
print(course.replace(' ','*'))

# Hello World karakter dizisinin World ifadesini There olarak degistirin
print('Hello World'.replace('World','There'))

# course karakter dizisini bosluk karakterlerinden ayirin
print(course.split(' '))