import math


def f_palin(n):
    numero = str(n)
    if numero == numero[::-1]:
        return True
    else:
        return False


def f_buscar(inf, sup):
    ninf = math.ceil(math.sqrt(inf))
    nsup = math.floor(math.sqrt(sup))
    sumas = 0
    for x in range(ninf, nsup + 1):
        if f_palin(x):
            if f_palin(pow(x,2)):
                sumas += 1
    return sumas


entrada = input()
casos = entrada
for x in range(int(casos)):
    entrada = input()
    arr = [int(s) for s in entrada.split(' ')]
    print('Caso #'+str(x+1)+': '+str(f_buscar(arr[0], arr[1])))
