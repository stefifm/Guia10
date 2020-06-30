print("Solo menores a siete")

def porcentaje (a, nt):
    p = (a * 100) / nt
    return p
def par(numero):
    if numero % 2 == 0:
        return True
    return False
def multiplo(n1, n2):
    resto = n1 % n2
    return resto == 0



n = int(input("Cargue una secuencia de números. Termina en cero: "))
cont_pares = 0
cont_total = 0
cont_digito = 0
flag_menor = False
while n != 0:
    cont_total += 1
    if par(n) == True:
        cont_pares += 1

    digito = n
    if n > 10:
        digito = n % 10
    if digito == 4 or digito == 5:
        cont_digito += 1

    if multiplo(n, 3):
        if flag_menor == False or n < menor:
            menor = n
            flag_menor = True