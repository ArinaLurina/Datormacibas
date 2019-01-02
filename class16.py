from math import fabs
from time import sleep
from numpy.ma import cosh


def f(x):
    return cosh(x / 2)
k=0
# Definejam argumenta x robezhas:
a = -100
b = 100

# Aprekjinam funkcijas vertibas dotajos punktos:
funa = f(a)
funb = f(b)

# Paarbaudam, vai dotajaa intervaalaa ir saknes:

if (funa*funb>0):
    print("Dotajaa intervaalaa [%s, %s] saknju nav" % (a, b))
    sleep(1);exit()
    exit()

# Zinjo uz ekraana, gaida 3 sec un darbu pabeidz

else:
    print("Dotajaa intervaalaa sakne(s) ir!")

# Defineejam precizitaati, ar kaadu mekleesim sakni:

deltax = 0.0001

# Sashaurinam saknes mekleeshanas robezhas :

while fabs(b - a) > deltax:
    k=k+1
    x = (a + b) / 2
    funx = f(x)
    if (funa * funx < 0.0):
        b = x
    else:
        a = x

print("Sakne ir:", x)
print("Iteraciju skaits:", k)
