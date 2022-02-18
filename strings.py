message = "Test mesaji"
print(message[-1])  # Eksi ile yazilan ifade sondan basa dogru karakter yazmamizi saglar
print(len(message))
print(message[0:5])
print(len(message[-1:-3]))
# Baslangic indeksi , bitis indeksinden kucuk olmalidir
# Bu yuzden bos metin dondurur
print(message[-10:-1])
print(message[::-1])  # Metni ters cevirir
