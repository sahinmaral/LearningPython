names = ['Ali','Yagmur','Hakan','Deniz']
years = [1998,2000,1998,1987]

# Cenk ismini listenin sonuna ekleyiniz
names.append('Cenk')

# Sena ismini listenin basina ekleyiniz
names.insert(0,'Sena')

# Deniz ismini listeden siliniz
names.remove('Deniz')

# Cenk isminin indeksi nedir
names.index('Cenk')

# Ali listenin bir elemani midir
print(names.__contains__('Ali'))

# Liste elemanlarini ters cevirin
print(names.reverse())

# Liste elemanlarini alfabetik olarak siralayiniz
print(names.sort())

# years listesini rakamsal buyukluge gore siralayiniz
print(years.sort())

# str = "Chevrolet,Dacia" karakter dizisini listeye ceviriniz
str = "Chevrolet,Dacia"
print(str.split(','))

# years dizisinin en buyuk ve en kucuk elemani nedir
print(min(years),max(years))

# years dizisinde kac tane 1998 degeri vardir
print(years.count(1998))

# years dizisinin tum elemanlarini siliniz
years.clear()

# Kullanicidan alacaginiz 3 tane marka bilgisini bir listede saklayiniz
brands = []
brand1 = input('Marka1 : ')
brand2 = input('Marka2 : ')
brand3 = input('Marka3 : ')

brands.append(brand1)
brands.append(brand2)
brands.append(brand3)
print(brands)