import matplotlib.pyplot as plt
from random import *
from numpy import *
import sys

#parametri
a = 0.5 # prirodni prirastaj
b = 0.5 # stopa umanjenja populacije vrste na osnovu uticaja toksina
c = 0.5 # stopa izumiranja toksina
d = 0.5 # stopa nastajanja toksina zavisi samo od kolicine populacije vrste
dt = 0.01 
max_time = 100

# pocetne tacke
t = 0
x = 2 
y = 1

#incijalizacija listi za cuvanje podataka
t_list = []; x_list = []; y_list = []

t_list.append(t); x_list.append(x); y_list.append(y)

while t < max_time:
    x_t = x                     # prilikom promene Y, mora se uzeti X(t), a ne X(t+dt)
    
    t = t + dt
    x = x + (a*x - b*x*y)*dt    #dX/dt = a*X - b*X*Y
    y = y + (d*x_t - c*y)*dt    #dY/dt = -c*Y + d*X

    t_list.append(t)
    x_list.append(x)
    y_list.append(y)

p = plt.plot(t_list, x_list, 'r', t_list, y_list, 'b', linewidth = 1.5)
plt.grid()
plt.legend(['Alge', 'Toksini'], loc='upper right')
plt.xlabel('vreme')
plt.ylabel('populacija')
p.title(f'MODEL: (a: {a}, b: {b}, c: {c}, d: {d}) \n ST: ({round((c*a) / (d*b), 2)}, {round(a/b, 2)})')
plt.show()
