import matplotlib.pyplot as plt
import numpy as np

"""
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y,color='red',linewidth='5')
plt.axis([0,6,0,20])

plt.title('Grafik basligi')
plt.xlabel('x label')
plt.ylabel('y label')
"""

"""
x = np.linspace(0,2,100)

plt.plot(x,x,label='linear' , color='red')
plt.plot(x,x**2,label='quadratic' , color='yellow')
plt.plot(x,x**3,label='cubic' , color='green')

plt.xlabel('x label')
plt.ylabel('y label')

plt.legend()
"""

"""
x = np.linspace(0,2,100)

fig, axis = plt.subplots(2)
axis[0].plot(x,x,color='red')
axis[0].set_title('Linear')

axis[1].plot(x,x**2,color='green')
axis[1].set_title('Quadratic')

plt.tight_layout()
"""

"""
x = np.linspace(0,2,100)
fig, axis = plt.subplots(2,2)
fig.suptitle('Grafik basligi')

axis[0,0].plot(x,x,color='red')
axis[0,1].plot(x,x**2,color='blue')
axis[1,0].plot(x,x**3,color='green')
axis[1,1].plot(x,x**4,color='yellow')
"""



plt.show()





