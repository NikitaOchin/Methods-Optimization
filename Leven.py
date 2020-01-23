import math
from sympy import diff,lambdify,symbols
import numpy as np
import numpy.linalg as ln

def levenberg(eps, M,x,F,f,f2):
    k,L,x = 0,20,np.array(x)
    k1 = 0
    while True:
        if ln.norm(f(x)) <= eps: return x,k,k1
        if k == M: return [None,None],M,0
        while True:
            k1+=1
            S = np.dot(ln.inv(f2(x)+ np.eye(2)*L),f(x))
            x1 = x - S
            if F(x1) < F(x):
                x, L = x1, 0.5*L
                k+=1
                break
            L = 2*L


def TestLeven():
    F = lambda x: (x[0] - 27)**4 + (x[0] - 2*x[1])**2
    f = lambda x: np.array([4*(x[0] - 27)**3 + 2*(x[0] - 2*x[1]),-4*(x[0] - 2*x[1])])
    f2 = lambda x: np.array([[12*(x[0] - 27)**2 + 2*x[0],-4],[-4,8*x[1]]])

    F = lambda x: 2*(x[0]**2) + x[0]*x[1] + (x[1]**2)
    f = lambda x: np.array([4*x[0] + x[1], 2*x[1] + x[0]])
    f2 = lambda x: np.array([[4,0],[0,2]])
    
    x,k,k1 = levenberg(0.1, 10, [0.5,1],F,f,f2)
    print("k = {}".format(round(k,5)))
    print("x = {}, {}".format(*x))
    print("F(x) = {}".format(round(F(x),5)))
    print("f1(x) = {}, {}".format(*f(x)))
    print("кол-во вычислений функции = {}".format(k1*2))
    print("кол-во вычислений градиента = {}".format(k1+k+1))
    print("кол-во вычислений матрицы Гессе = {}".format(k1+k))

if __name__ == '__main__':
    TestLeven()
            
        

        
