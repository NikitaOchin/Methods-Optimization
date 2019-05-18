import math
from sympy import diff,lambdify,symbols
import numpy

def Nuiton_Extr(F,x0,delta):
    """Метод Ньютона поиска минимума функции F
       F - искомая функция
       f - производная функции F
       f2 - вторая производная функции F
       x0 - начальня точка
       delta - точность"""
    
    X = symbols('x')
    f = lambdify(X, diff(F(X)))
    f2 = lambdify(X, diff(f(X)))
    x = x0 - f(x0)/f2(x0)
    k = 1
    
    while math.fabs(f(x)) >= delta:
        x = x - f(x)/f2(x)
        k+=1
    else: return x,k

def TestNuiton():
    F = lambda x: x**5 - x**2
    
    x0 = 1
    delta = 0.10E-4
    x,k = Nuiton_Extr(F,x0,delta)
    s = "При x0 = {}, delta = {}\n".format(x0,delta)
    s+= "{0:0.5f} - точка минимума\n".format(x)
    s+= "{0:0.5f} - зн-е ф-ии в этой точке\n".format(F(x))
    s+= "{} - кол-во итераций\n".format(k)
    s+= "{} - кол-во вычислений первой производной\n".format(2*k-1)
    s+= "{} - кол-во вычислений второй производной\n".format(k-1)
    print(s)

    F = lambda x: x**4
    x0 = 1
    delta = 0.75
    x,k = Nuiton_Extr(F,x0,delta)
    s = "При x0 = {}, delta = {}\n".format(x0,delta)
    s+= "{0:0.5f} - точка минимума\n".format(x)
    s+= "{0:0.5f} - зн-е ф-ии в этой точке\n".format(F(x))
    s+= "{} - кол-во итераций\n".format(k)
    s+= "{} - кол-во вычислений первой производной\n".format(2*k-1)
    s+= "{} - кол-во вычислений второй производной\n".format(k-1)
    print(s)

if __name__ == "__main__":
    TestNuiton()
