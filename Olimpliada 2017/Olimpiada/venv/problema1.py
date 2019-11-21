def f_totito(matriz):
    elementos = set()
    revisar = ['f', 'c', 'd']
    ganaron = False
    for x in revisar:
        if x == 'f':
            for f in range(4):
                fila = set()
                for j in range(4):
                    caracter = matriz[f][j]
                    fila.add(caracter)
                    elementos.add(caracter)
                if fila == {'X'} or fila == {'X', 'T'}:
                    ganaron = True
                    return 'X'
                    break
                elif fila == {'O'} or fila == {'O', 'T'}:
                    ganaron = True
                    return 'O'
                    break
            if ganaron:
                break
        elif x == 'c':
            for c in range(4):
                fila = set()
                for j in range(4):
                    caracter = matriz[j][c]
                    fila.add(caracter)
                    elementos.add(caracter)
                if fila == {'X'} or fila == {'X', 'T'}:
                    ganaron = True
                    return 'X'
                    break
                elif fila == {'O'} or fila == {'O', 'T'}:
                    ganaron = True
                    return 'O'
                    break
            if ganaron:
                break
        elif x == 'd':
            for f in range(2):
                if f == 0:
                    fila = set()
                    for j in range(4):
                        caracter = matriz[j][j]
                        fila.add(caracter)
                        elementos.add(caracter)
                    if fila == {'X'} or fila == {'X', 'T'}:
                        ganaron = True
                        return 'X'
                        break
                    elif fila == {'O'} or fila == {'O', 'T'}:
                        ganaron = True
                        return 'O'
                        break
                else:
                    fila = set()
                    for j in range(4):
                        caracter = matriz[j][-1-j]
                        fila.add(caracter)
                        elementos.add(caracter)
                    if fila == {'X'} or fila == {'X', 'T'}:
                        ganaron = True
                        return 'X'
                        break
                    elif fila == {'O'} or fila == {'O', 'T'}:
                        ganaron = True
                        return 'O'
                        break
    if not(ganaron):
        if '.' in elementos:
            return 'El juego no ha terminado'
        else:
            return 'Draw'


def f_leer_matriz(n = 4):
    matriz = []
    for j in range(n):
        entrada = input()
        if entrada == '':
            j = j - 1
        else:
            fila = [s for s in list(entrada)]
            matriz.append(fila)
    return matriz


casos = int(input())
for x in range(casos):
    matriz = f_leer_matriz()
    resultado = f_totito(matriz)
    if resultado == 'X' or resultado == 'O':
        print('Caso #'+str(x+1)+': '+resultado+' gano')
    else:
        print('Caso #'+str(x+1)+ ': '+resultado)
