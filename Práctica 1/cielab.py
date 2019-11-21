from random import randrange


def mala_resta(arreglo):
    resta = arreglo[0] - arreglo[1]
    numero = str(resta)
    i = randrange(len(numero))
    arr_numero = list(numero)
    digito = int(arr_numero[i])
    suma = randrange(9)
    digito = (digito + suma)%10
    if i == 0 and digito == 0:
        digito = (digito + suma)%10
    arr_numero[i] = str(digito)
    numero = int(''.join(arr_numero))
    print(numero)


try:
    original = input()
    arreglo = [int(s) for s in original.split()]
    mala_resta(arreglo)
except EOFError:
    pass