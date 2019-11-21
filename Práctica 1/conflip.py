import math
try:
    casos = int(input())
    for i in range(casos):
        juegos = int(input())
        for j in range(juegos):
            condiciones = input()
            arreglo = [int(s) for s in condiciones.split(' ')]
            if arreglo[0] == arreglo [2]:
                print(math.floor(arreglo[1]/2))
            else:
                print(math.ceil(arreglo[1]/2))
except EOFError:
    pass