from numpy import *
import pylab as p

# parametri 
a = 0.8 # natalitet algi
b = 0.6
c = 0.2 # mortalitet toksina
d = 0.3

#dx/dt = a*x - b*x*y
#dy/dt = -c*y + d*x*y
def dX_dt(X, t=0):
    return array([ a*X[0] - b*X[0]*X[1] ,  
                  -c*X[1] + d*X[0]*X[1] ])

# stacionarne tacke
X_f0 = array([ 0., 0.])
X_f1 = array([ c/d, a/b])


from scipy import integrate

# time
t = linspace(0, 50,  1000)
# initials conditions:
X0 = array([2, 1])

X = integrate.odeint(dX_dt, X0, t)

algae, toxins = X.T

f1 = p.figure()
p.plot(t, algae, 'r-', label='Algae')
p.plot(t, toxins  , 'b-', label='Toxins')
p.grid()
p.legend(loc='upper right')
p.xlabel('time')
p.ylabel('population')
p.title(f'a: {a}, b: {b}, c: {c}, d: {d}')
f1.savefig('./plots/model2.png')
p.show()
