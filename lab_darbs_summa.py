# -*- coding: utf-8 -*-
from math import cos

def mans_kosinuss(x):
    k = 0
    a = x**0/(1)
    S = a
    print("Izdruka no liet.f. a0 = %6.2f S0 = %6.2f"%(a,S))
    
    while k < 500:
        k = k + 1
        R = x*x/((2*k-1)*(2*k)*4)
        a = a * R
        S = S + a
        if k == 499:
            print("Izdruka no liet.f. a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
    
    S = S + a
    print("Izdruka no liet.f. a500 = %6.2f S500 = %6.2f"%(a,S))
    return S

x = float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
y = cos(x)
print("standarta cos(%.2f) = %6.2f"%(x,y))


yy = mans_kosinuss(x)
m = u"\u221E"
print("mans cos(%.2f) = %6.2f"%(x,yy))



print("    500                                            ")
print("   _____                                           ")
print("   \                                               ")
print("    \         x**2*k                               ")
print("     >   _________________, kur -%s<x<%s"%(m,m))   
print("    /                                              ")
print("   /      (2*k)! * 2**2*k                          ")
print("  ______                                           ")
print("     k = 0                                         ")


print("                             x*x       ")
print(" rekurences reizinatajs:  ____________ ")
print("                                       ")
print("                         (2k-1)(2k)*4  ")
