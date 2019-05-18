def Extr_Dixot(f, a, b, eps, delta):
    """Дихотомический метод нахождения экстремума функции
    f - принимаемая функция
    a - начало отрезка
    b - конец отрезка
    eps - константа различимости
    delta - точность конечного результата
    """
    k = 1
    while True:
        c = (a+b)/2
        if b-a < delta: return c,k
        l,m = c+eps, c-eps
        if f(l) > f(m): b = l
        else: a = m
        k+=1

def SolotSech_Extr(f,a,b,delta):
    """Метод золотого сечения для нахождение экстремума функции
    f - принимаемая функция
    a - начало отрезка
    b - конец отрезка
    eps - константа различимости
    delta - точность конечного результата
    """
    k = 1
    while True:
        if b-a < delta: return (b+a)/2,k
        l,m = a+(b-a)*0.382, a+(b-a)*0.618
        if f(l) > f(m): a = l
        else: b = m
        k+=1

def Test():
    F = lambda x: x**5 - x**2

    eps = 0.10E-6
    a,b = 0.5, 1
    delta = 0.10E-4
    x,k = Extr_Dixot(F,a,b,eps,delta)
    s = "Дихотомический метод поиска экстремума функции х^5 - х^2\n"
    s+= "При a = {}, b = {}, delta = {}, eps = {}\n".format(a,b,delta,eps)
    s+= "{0:0.5f} - точка минимума\n".format(x)
    s+= "{0:0.5f} - зн-е ф-ии в этой точке\n".format(F(x))
    s+= "{} - кол-во итераций\n".format(k)
    print(s)

    F = lambda x: x**5 - x**2
    a,b = 0, 1
    delta = 0.01
    x,k = SolotSech_Extr(F,a,b,delta)
    s = "Метод золотого сечения для поиска экстремума функции х^5 - х^2\n"
    s+= "При a = {}, b = {}, delta = {}\n".format(a,b,delta)
    s+= "{0:0.5f} - точка минимума\n".format(x)
    s+= "{0:0.5f} - зн-е ф-ии в этой точке\n".format(F(x))
    s+= "{} - кол-во итераций\n".format(k)
    print(s)

if __name__ == "__main__":
    Test()
