import pandas as pd

df = pd.read_csv("imdb.csv")

# Dosya hakkindaki bilgiler
result = df
result = df.columns

# Ilk 5 kaydi gosterin
result = df.head()

# Ilk 10 kaydi gosterin
result = df.head(10)

# Son 5 kaydi gosterin
result = df.tail()

# Son 10 kaydi gosterin
result = df.tail(10)

# Sadece Title kolonunu alin
result = df['Title']

# Sadece Title kolonunu iceren ilk 5 kaydi alin
result = df['Title'].head()

# Sadece Title ve Rating kolonunu iceren ilk 5 kaydi alin
result = df[['Title','imdbRating']].head()

# Sadece Title ve Rating kolonunu iceren son 7 kaydi alin
result = df[['Title','imdbRating']].tail(7)

# Sadece Title ve Rating kolonunu iceren ikinci 5 kaydi alin
result = df[['Title','imdbRating']][5:15]

# Sadece Title ve Rating kolonunu iceren ve 
# imdb puani (imdbRating) 8.0 ve ustunde olan kayitlardan ilk 50 tanesini aliniz
result = df.query('imdbRating > 8.0')[['Title','imdbRating']].head(50)

# Yayin tarihi 2014 ile 2015 arasinda olan filmlerin isimlerini getiriniz
result = df.query('Year >= 2014 & Year <= 2015')['Title']

# Degerlendirme sayisi 100.000 den buyuk 
# ya da imdb puani 8 ile 9 arasinda olan filmleri listeleyiniz

imdbVotesColumn = df['imdbVotes'].replace(',','', regex=True).astype(int) > 100000

result =  imdbVotesColumn | ((df['imdbRating'] >= 8) & (df['imdbRating'] <= 9))

result = df[result]['Title']

print(result)