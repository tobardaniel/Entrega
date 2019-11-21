def f_dinero(rides, cupo, grupos):
    n = len(grupos)
    gente = sum(grupos)
    dinero = 0
    if gente <= cupo:
        dinero = gente * rides
    else:
        patron = True
        vueltas = 0
        i = 0
        while vueltas < rides and patron:
            ocupados = 0
            for x in range(n):
                if ocupados + grupos[i % n] <= cupo:
                    ocupados = ocupados + grupos[i % n]
                    i = i + 1
                else:
                    break
            dinero += ocupados
            vueltas += 1
    return dinero




casos = int(input())
for x in range(casos):
    arreglo = [int(s) for s in input().split()]
    r = arreglo[0]
    k = arreglo[1]
    grupos = [int(s) for s in input().split()]
    resultado = f_dinero(r, k, grupos)
    caso = str(x + 1)
    print('Caso #'+str(caso)+': ' + str(resultado))