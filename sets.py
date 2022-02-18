fruits = {'orange','apple','banana'}

# print(fruits[0])

# Set listesi , bir nevi matematikteki kumeler gibidir
# Rastgele siralanmistir ve herhangi bir indeks numaralari yoktur
# Ayni nesneden defalarca eklenildiginde ayni nesne eklenmez

for x in fruits :
    print(x)

fruits.update(['grape','melon','apple'])
print(fruits)

myList = [1,1,3,4]
print(set(myList))

# Remove ile discard arasindaki fark 
# Remove edilecek nesne , silinecek listede yoksa hata dondurur
# Discard uzerinde herhangi bir sey yapmaz
fruits.remove('grape')
fruits.discard('melon')


