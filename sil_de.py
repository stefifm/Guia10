print("Sílaba de")

def es_digitos(n):
    digitos = "0123456789"
    if n in digitos:
        return True
    return False


cont_digitos = 0
cont_letras = 0
pal_digitos = 0
pal_tres_menos = 0
pal_cuatro_seis = 0
pal_mas_seis = 0
palabra = 0
flag_de = flag_d = False
cont_de = 0
pos_de = 0
texto = input("Ingrese un texto. Termina con punto: ")

for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        if es_digitos(caracter):
            cont_digitos += 1
        if caracter == "d":
            flag_d = True
        else:
            if flag_d and caracter == "e":
                flag_de = True
                pos_de = cont_letras
            flag_d = False
    else:
        if cont_letras == 0:
            continue
        palabra += 1
        if cont_digitos == 1:
            pal_digitos += 1
        if cont_letras <= 3:
            pal_tres_menos += 1
        else:
            if cont_letras == 4 or cont_letras == 6:
                pal_cuatro_seis += 1
            else:
                if cont_letras > 6:
                    pal_mas_seis += 1
        if palabra == 1 or cont_letras > mayor:
            mayor = cont_letras
        if flag_de and pos_de <= (cont_letras // 2):
            cont_de += 1
        cont_letras = 0
        cont_digitos = 0
        flag_de = False

print("Palabras con al menos un dígito:",pal_digitos)
print("Cantidad de palabras menor o igual a tres letras:",pal_tres_menos)
print("Cantida de palabras que tenína 4 y hasta 6 letras:",pal_cuatro_seis)
print("Cantidad de palabras que tenían más de 6 letras:",pal_mas_seis)
print("La longitud de la palabra más larga:",mayor)
print("Cantidad de palabras que tienen la sílaba de en la primera mitad:",
      cont_de)

