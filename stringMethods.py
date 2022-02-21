message = ' Hello there. My name is Sahin Maral '

print(message.upper())
print(message.lower())

# Her kelimenin ilk harfi buyuk harf olur
print(message.title()) 

# Ilk kelime haric her kelimenin ilk harfi kucuk harf olur
print(message.capitalize()) 

# Bastaki ve sondaki bosluklari siler
print(message.strip())

# Kelimeler , dizilere ayrilir
print(message.split())

# Dizi icerisinde olan kelimeleri birlestirir
splitMessage = message.split()
print(' '.join(splitMessage))

# Metin icerisindeki kelimeyi arar ve 
# baslangic indeksini dondurur , bulamazsa -1 dondurur
print(message.find('Sahin'))

# 100 karakterli bir metin icerisinde metnimizi ortalar
print(message.center(100,'*'))

code = 'print("hello world")'
eval(code) # Sadece bir ifade kabul eder
exec(code) # Birden fazla ifadeyi kabul eder

print(abs(-42))