import math
from sympy import diff,lambdify,symbols
import numpy

def Balcano_Extr(F,a,b,delta):
    """Метод Бальцано (средней точки) поиска минимума функции F
       a - начало данного отрезка
       b - конец данного отрезка
       F - искомая функция
       f - производная функции F
       delta - точность"""
    
    x = symbols('x')
    f = lambdify(x, diff(F(x)))
    k = 1
    
    while True:
        ck = (a+b)/2
        if math.fabs(f(ck)) < delta:
            return ck,k
        if f(ck) > 0: b = ck
        else: a = ck
        k+=1
        #if k > 10000: print("Error");return 0,0


def TestBalcano():
    F = lambda x: x**5 - x**2
    
    a,b = 0.5, 1
    delta = 0.10E-4
    x,k = Balcano_Extr(F,a,b,delta)
    s = "При a = {}, b = {}, delta = {}\n".format(a,b,delta)
    s+= "{0:0.5f} - точка минимума\n".format(x)
    s+= "{0:0.5f} - зн-е ф-ии в этой точке\n".format(F(x))
    s+= "{} - кол-во итераций\n".format(k)
    s+= "{} - кол-во вычислений производной\n".format(2*k-1)
    print(s)

    F = lambda x: x**2
    a,b = -2, 1
    delta = 0.1
    x,k = Balcano_Extr(F,a,b,delta)
    s = "При a = {}, b = {}, delta = {}\n".format(a,b,delta)
    s+= "{0:0.5f} - точка минимума\n".format(x)
    s+= "{0:0.5f} - зн-е ф-ии в этой точке\n".format(F(x))
    s+= "{} - кол-во итераций\n".format(k)
    s+= "{} - кол-во вычислений производной\n".format(2*k-1)
    print(s)

if __name__ == "__main__":
    TestBalcano()
