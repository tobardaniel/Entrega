def min_dif(arreglo):
    arreglo.sort()
    a=arreglo[1]-arreglo[0]
    for i in range(0,len(arreglo)-1):
        if arreglo[i+1]-arreglo[i] < a:
            a = arreglo[i+1]-arreglo[i]
    print(a)


try:
    casos = int(input())
    for i in range(casos):
        caballos = int(input())
        habilidades = input()
        arreglo = [int(s) for s in habilidades.split(' ', caballos)]
        min_dif(arreglo)
except:
    pass