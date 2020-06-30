def prueba(n):
    r = ()
    for i in range(0, n+1, 4):
        r += i,
    return r
def test():
    n = int(input("Cargue un número: "))
    resultado = prueba(n)
    print("divisibless a 4 y 5:",resultado)
test()