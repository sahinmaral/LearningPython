website = 'https://www.sadikturan.com'
kursAdi = 'Python Dersleri: Sifirdan Ileri Seviye Python Programlama'

# kursAdi karakter dizisinde kac karakter bulunmaktadir
print(len(kursAdi))

# website icinden www karakterlerini aliniz
print(website[8:11])

# website icinden com karakterlerini aliniz
print(website[-3:])

# kursAdi icinden ilk 15 ve son 15 karakterini alin
print(f'kursAdi ilk 15 karakter : {kursAdi[0:15]}')
print(f'kursAdi son 15 karakter : {kursAdi[-15:]}')

# kursAdi ifadesindeki karakterleri tersten yazdirin
print(kursAdi[::-1])

# Hello world ifadesindeki w harfini W ile degistirin
text = 'Hello world'
text = text[0:6] + 'W' + text[7:]
print(text)

# abc ifadesini yan yana 3 defa yazdirin
print('abc' * 3)

name , surname , age , job = 'Sahin' , 'Maral' , 22 , 'Bilgisayar Muhendisligi'

# Yukarida verilen degiskenler ile ekrana asagidaki ifadeyi yazdirin
# Benim adim Sahin Maral , Yasim 22 ve meslegim Bilgisayar Muhendisligi

print(f'Benim adim {name} {surname} , Yasim {age} ve meslegim {job}')