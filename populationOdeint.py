from numpy import *
import pylab as p

# parametri 
a = 0.5 # prirodni prirastaj
b = 0.5 # stopa umanjenja populacije vrste na osnovu uticaja toksina
c = 0.5 # stopa izumiranja toksina
d = 0.5 # stopa nastajanja toksina zavisi samo od kolicine populacije vrste

#dX/dt = a*X - b*X*Y
#dY/dt = -c*Y + d*X
def dX_dt(X, t=0):
    return array([ a*X[0] - b*X[0]*X[1] ,  
                  -c*X[1] + d*X[0]      ])

# stacionarne tacke
print(f'Stacionarne tacke : {(c*a) / (d*b)}, {a/b}')
X_f1 = array([ (c*a) / (d*b), a/b])


from scipy import integrate

# vreme
t = linspace(0, 100,  1000)
# pocetne tacke
X0 = array([2, 1])

X = integrate.odeint(dX_dt, X0, t)

algae, toxins = X.T

f1 = p.figure()
p.plot(t, algae, 'r-', label='Alge')
p.plot(t, toxins  , 'b-', label='Toksini')
p.grid()
p.legend(loc='upper right')
p.xlabel('vreme')
p.ylabel('populacija')
p.title(f'a: {a}, b: {b}, c: {c}, d: {d}')
#f1.savefig('./plots/model1.png')
p.show()

#############################################################################################
'''
#vrednosti izmedju dve stacionarne tacke (0, c/d)
values  = linspace(0, 3, 8)
vcolors = p.cm.autumn_r(linspace(0., 1., len(values)))
f2 = p.figure()

#trajektorije
for v, col in zip(values, vcolors): 
    X0 = v * X_f1 #startna tacka
    X = integrate.odeint( dX_dt, X0, t)
    p.plot( X[:,0], X[:,1], lw=v, color=col, label=f'A:{int(X0[0])}, T:{int(X0[1])}')


# definisanje mreze
ymax = p.ylim(ymin=0)[1]
xmax = p.xlim(xmin=0)[1]
nb_points   = 20                      

x = linspace(0, xmax, nb_points)
y = linspace(0, ymax, nb_points)

X1 , Y1  = meshgrid(x, y)
DX1, DY1 = dX_dt([X1, Y1])
M = (hypot(DX1, DY1))
M[ M == 0] = 1.
DX1 /= M
DY1 /= M                                  

#iscrtavanje grafika
p.title(f'Trajectories: a: {a}, b: {b}, c: {c}, d: {d}')
Q = p.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=p.cm.jet)
p.xlabel('Alge')
p.ylabel('Toksini')
p.legend()
p.grid()
p.xlim(0, xmax)
p.ylim(0, ymax)
p.show()
#f2.savefig('plots/populations.png')
'''
