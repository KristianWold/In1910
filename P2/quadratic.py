import numpy as np
import matplotlib.pyplot as plt
import math as m

#1a)
class Quadratic():
    def __init__(self, a2, a1, a0):
        self.a2 = a2;
        self.a1 = a1;
        self.a0 = a0;
    def __call__(self,x):
        return self.a2*x**2 + self.a1*x + self.a0
    #1b)
    def __str__(self):
        return "%.2f x^2 + %.2f x + %.2f"%(self.a2, self.a1, self.a0)
    #1c)
    def __add__(self,other):
        a2 = self.a2 + other.a2
        a1 = self.a1 + other.a1
        a0 = self.a0 + other.a0
        return Quadratic(a2, a1, a0)
    #1d)
    def roots(self):
        a2 = self.a2; a1 = self.a1; a0 = self.a0
        rad = a1**2-4*a2*a0
        if rad > 0:
            return ((-a1 + m.sqrt(rad))/(2*a2),(-a1 - m.sqrt(rad))/(2*a2))
        elif rad == 0:
            return (-a1/(2*a2),)
        else:
            return ()
    #1e)
    def intersect(self,g):
        a2 = self.a2 - g.a2
        a1 = self.a1 - g.a1
        a0 = self.a0 - g.a0
        h = Quadratic(a2,a1,a0)
        return h.roots()


"""
f = Quadratic(1, -2, 1)
print(f)
x = np.linspace(-5, 5, 101)
plt.plot(x, f(x))
plt.show()
"""

"""
f = Quadratic(1, -2, 1)
g = Quadratic(-1, 6, -3)

h = f + g
print(h)

x = np.linspace(-5, 5, 101)
plt.plot(x, h(x))
plt.show()
"""
"""
f1 = Quadratic(2,-2,2)
f2 = Quadratic(1,-2,1)
f3 = Quadratic(1,-3,2)

print(f1.roots())
print(f2.roots())
print(f3.roots())
"""
f = Quadratic(1,-2,1)
g = Quadratic(2,3,-2)
print(f.intersect(g))
