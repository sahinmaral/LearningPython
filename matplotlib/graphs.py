import matplotlib.pyplot as plt
import numpy as np

yil = [2011, 2012, 2013, 2014, 2015]

oyuncu1 = [8, 10, 12, 7, 9]
oyuncu2 = [7, 12, 5, 15, 21]
oyuncu3 = [18, 20, 22, 25, 19]

# Stack Plot

"""
plt.plot([],[],color='y',label='oyuncu1')
plt.plot([],[],color='r',label='oyuncu2')
plt.plot([],[],color='b',label='oyuncu3')

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=['y','r','b'])
plt.title('Yillara gore atilan goller')

plt.xlabel('Yil')
plt.ylabel('Gol sayisi')

plt.legend()
"""

# Donut plot

"""
goal_types = 'Penalti','Kaleye atilan sut','Serbest Vurus'
goals = [12,35,7]

colors = ['y','r','b']

plt.pie(goals,labels=goal_types,colors=colors , shadow=True, explode=(0.05,0.05,0.05), autopct='%1.1f%%')
"""

# Bar plot

"""
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label='BMW', width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label='Audi', width=.5)

plt.legend()
plt.xlabel('Gun')
plt.ylabel('Mesage (km)')
plt.title('Arac bilgileri')
"""

# Histogram plot

"""
yaslar = [78, 6, 84, 73, 47, 32, 27, 17, 10,
          42, 35, 71, 89, 85, 54, 36, 47, 38, 61, 1]

yas_gruplari = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(yaslar,yas_gruplari,histtype='bar',rwidth=.8)
plt.xlabel('Yas gruplari')
plt.ylabel('Kisi sayisi')
plt.title('Histogram')
"""

plt.show()
