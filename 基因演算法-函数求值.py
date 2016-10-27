#f(x1, x2) = 21.5 + x1*sin(4*pi*x1) + x2*sin(20*pi*x2)
from math import sin
from math import pi

def fun(x1, x2):
    value = 21.5 + x1*sin(4*pi*x1) + x2*sin(20*pi*x2)
    return value

Max = fun(12.1, 5.8)
precise = 0.00001
x1 = m = 12.1
x2 = n = 5.8

while(m >= -3):
    while(n >= 4.1):
        temp = fun(m, n)
        if(temp > Max):
            Max = temp
            x1 = m
            x2 = n
        n = n - precise
    m = m - precise


print("when x1 = "+repr(m)+", x2 = "+repr(n)+", f(x1,x2) get MaxValue "+ repr(Max))


