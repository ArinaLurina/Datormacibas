#print(vars())
import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
#print(vars())

from numpy import sin, linspace
#print(vars())

def f(x):
    return sin(x) 


x = linspace(0,4,11)
#print(vars())

y = sin(x)
legend = []
print(legend)

from matplotlib import pyplot as plt
#print(plt.plot._doc_)
plt.axis([0,4,-1,1])
plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funcija $sin(x)$ un taas atvasinaajumi")
plt.plot(x,y,"k")
legend.append("$sin(x)$ - default - viss ir savienots ar taisnaam liinijaam")
#print(legend)
plt.plot(x,y,"ro")
legend.append("$sin(x)$ - tikai dazhi punkti")
#print(legend)

N = len(x)
deltax = x[1] - x[0]
derivative = []

for i in range (N):
    temp = (f(x[i] + deltax) - f(x[i])) /deltax
    derivative.append(temp)

plt.plot(x,derivative,"y")
legend.append("$sin(x)$atvasinaajums - viss ir savienots ar taisnaam liinijaam")
plt.plot(x,derivative,"go")
legend.append("$sin(x)$ atvasinaajums - dashi punkti")

derivative_through_array = []

for i in range(N-1):
    temp = (y[i+1] - y[i]) / (x[i+1] - x[i])
    derivative_through_array.append(temp)


plt.plot(x[0:N-1],derivative_through_array,"m")

plt.plot(x,derivative,"m")
legend.append("$sin(x)$atvasinaajums, izmantojot masiva veertiibas - viss ir savienots ar taisnaam liinijaam")
plt.plot(x,derivative,"bo")
legend.append("$sin(x)$ atvasinaajums,izmantojot massiva vertiibas - dashi punkti")









plt.plot(.680,0.620,"ch",markersize = 20)
#print(plt.legend._doc)
#plt.legend(legend, loc = upper left")
plt.legend(legend, loc = 3, fancybox=True, framealpha=0.05)
plt.show()



