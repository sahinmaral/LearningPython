from random import randint
import numpy as np

# 1 - (10,15,30,45,60) degerlerine sahip numpy dizisi olusturunuz

result = np.array([10,15,30,45,60])
print(result)

# 2 - (5-15) arasindaki sayilarla numpy dizisi olusturunuz

result = np.arange(5,15)
print(result)

# 3 - (50,100) arfasinda 5'er 5'er artarak numpy dizisi olusturunuz

result = np.arange(50,100,5)
print(result)

# 4 - 10 elemanli sifirlardan olusan bir dizi olusturunuz

result = np.zeros(10)
print(result)

# 5 - 10 elemanli birlerden olusan bir dizi olusturunuz

result = np.ones(10)
print(result)

# 6 - (0,100) arasinda esit aralikli 5 sayi uretin

result = np.linspace(0,100,5)
print(result)

# 7 - (10,30) arasinda rastgele 5 tane tamsayi uretin

result = np.random.randint(10,30,5)
print(result)

# 8 - (-1,1) arasinda rastgele 10 tane sayi uretin

result = np.random.randn(10)
print(result)

# 9 - (3x5) boyutlarinda (10,50) arasinda rastgele bir matris olusturunuz

matris = np.random.randint(10,50,15).reshape(3,5)
print(result)

# 10 - Yukarida uretilen matriksin satir ve sutun sayilari toplamlarini hesaplayiniz
rowTotal = matris.sum(axis=1)
colTotal = matris.sum(axis=0)

print(rowTotal,colTotal)

# 11 - Yukarida uretilen matrisin en buyuk , en kucuk ve ortalamasi nedir

maximum_number = matris.max()
minimum_number = matris.min()
average_number = matris.mean()

print(maximum_number,minimum_number,average_number)

# 12 - Uretilen matrisin en buyuk degerinin indeksi nedir

maximum_number_index = matris.argmax()
print(maximum_number_index)

# 13 - (10,20) arasindaki sayilari iceren dizinin ilk 3 elemanini seciniz

indexing_random = np.arange(10,20)
print(indexing_random[:3])

# 14 - Yukaruda uretilen dizinin elemanlarini tersten yaziniz

print(indexing_random[::-1])

# 15 - Asagida uretilen matrisin ilk satirini seciniz

result = np.random.randint(10,50,15).reshape(3,5)
print(result[0])

# 16 - Yukarida uretilen matrisin 2.satir 3.sutundeki elemani hangisidir

print(result[2][3])

# 17 - Yukarida uretilen matrisin tum satirlardaki ilk elemani seciniz hangisidir

print(result[:,0])

# 18 - Yukarida uretilen matrisin her bir elemaninin karesini aliniz

result = result ** 2
print(result)

# 19 - Yukarida uretilen matris elemanlarinin hangisi pozitif cift sayidir

positive_even_numbers = result[result % 2 == 0]
print(positive_even_numbers)

# 20 - Yukarida 