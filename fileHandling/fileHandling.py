'''
Dosya acmak ve olusturmak icin open() fonksiyonu kullanilir
Kullanimi: open(dosya_adi,dosya_erisme_modu)

'w' : (Write) yazma modu. Dosyayi konumda olusturur
'a' : (Append) ekleme. Dosya konumda yoksa olusturur
'x' : (Create) olusturma. Dosya zaten varsa hata verir
'r' : (Read) okuma. Varsayilan erisme modu parametresi.
    Dosya konumda yoksa hata verir.
'''

# file = open('fileHandling/test.txt','w')
# file.close()


# file = open('fileHandling/test.txt','w',encoding='utf-8')
# file.write('Sahin MARAL')
# file.close()

# file = open('fileHandling/test.txt','a',encoding='utf-8')
# file.write('\nSahin MARAL')
# file.close()

# try:
#     file = open('fileHandling/test.txt','r')
#     # text = file.read(10)
#     # text = file.read()
#     # print(text)

#     print(file.readline(),end='')
#     print(file.readline(),end='')
#     texts = file.readlines()
#     print(texts[0])
#     print(texts[1])
    
#     file.close()
# except FileNotFoundError as exception:
#     print(exception)


# with open('fileHandling/test.txt','r') as file:
#     content = file.read()
#     print(content)

#     # okuma bittikten sonra imlec , en sonda yer alir
#     # seek metodu ile imleci farkli konumlara koyabiliriz.
#     file.seek(0) 
#     print(content)
#     # okuma yaparken imlecin oldugu yeri gosterir
#     print(file.tell()) 

# with open('fileHandling/test.txt','r+',encoding='utf-8') as file:
#     print(file.read())
#     file.write('\nhello world')

# Sayfa basinda guncelleme

# with open('fileHandling/test.txt','r+',encoding='utf-8') as file:
#     content = file.read()
#     content = 'Efe Turan\n' + content
#     file.seek(0)
#     file.write(content)

with open('fileHandling/test.txt','r+',encoding='utf-8') as file:
    list = file.readlines()
    list.insert(2,'Melih SÖNMEZ\n')
    file.seek(0)
    file.writelines(list)

with open('fileHandling/test.txt','r+',encoding='utf-8') as file:
    print(file.read())