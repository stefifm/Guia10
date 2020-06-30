print("Ejercicio lalelilolu")

def promedio(al, p):
    prom = al / p
    return prom
def es_vocal(c):
    vocales = "aeiouAEIOU"
    if c in vocales:
        return True
    return False


cont_letras = 0
palabra = 0
acu_letras = 0
final_vocal = 0
caranterior = ""
l = False
flag_lalelilolu = False
pal_lalelilolu = 0
texto = input("Cargue un texto: Termina en punto: ")
texto = texto.lower()
for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if caracter == "l":
            l = True
        if l and es_vocal(caracter):
            flag_lalelilolu = True
    else:
        if cont_letras == 0:
            continue
        palabra += 1
        acu_letras += cont_letras
        if es_vocal(caranterior):
            final_vocal += 1
        if palabra == 1 or cont_letras > mayor:
            mayor = cont_letras
            orden = palabra
        if flag_lalelilolu == True:
            pal_lalelilolu += 1
        cont_letras = 0
        l = flag_lalelilolu = False




prom_letras = promedio(acu_letras, palabra)

print("Promedio de letras por palabra:",prom_letras)
print("Cantidad de palabras terminadas en vocal:",final_vocal)
print("La palabra más larga tiene",mayor,"y está en el orden",orden)
print("Cantidad de palabras con l+vocal:",pal_lalelilolu)