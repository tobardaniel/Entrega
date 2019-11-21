import math
try:
    casos = int(input())
    numeros = [int(input()) for s in range(casos)]
    for i in range(casos):
        numero = numeros[i]
        ceros = 0
        for j in range(13):
            ceros = ceros + math.floor(numero / (5 ** (j + 1)))
        print(ceros)
except EOFError:
    pass