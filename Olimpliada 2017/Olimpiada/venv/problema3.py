class Cofres():
    def __init__(self, tipo, llaves = []):
        self.tipo = tipo
        self.llaves = llaves
    def agarrar(self, llavero):
        pruebas = llavero
        for l in self.llaves:
            posicion = -1
            existe = False
            for j in pruebas:
                posicion += 1
                if l[0] == j[0]:
                    existe = True
                    break
            if existe:
                pruebas[posicion][1] = pruebas[posicion][1] + l[1]
            else:
                pruebas.append(l)
        return pruebas
    def abrir(self, llavero):
        pruebas = llavero
        abierto = False
        for llav in pruebas:
            if llav[0] == self.tipo:
                if llav[1] == 1:
                    pruebas.remove(llav)
                else:
                    llav[1] = llav[1] - 1
                abierto = True
                pruebas = self.agarrar(pruebas)
                break
        return [abierto, pruebas]


def f_abrir(cofres, llavero):
    solucion = []
    cofrerias = cofres
    if cofrerias != []:
        if llavero == []:
            solucion = 'IMPOSIBLE'
        else:
            for cof in cofres:
                cofre = cof[0]
                n_cofre = cof[1]
                llavero_c = llavero
                abierto = cofre.abrir(llavero_c)
                if abierto[0]:
                    cofrerias_c = cofrerias
                    solucion_c = solucion
                    llavero_c = abierto[1]
                    cofrerias_c.remove(cof)
                    solucion_c.append(n_cofre)
                    res = f_abrir(cofrerias_c, llavero_c)
                    if res != 'IMPOSIBLE':
                        cofrerias = cofrerias_c
                        solucion = solucion_c
                        llavero = llavero_c
                        for s in res:
                            solucion.append(s)
                        break
                    else:
                        solucion = res
    return solucion


def f_leer_llaves(arr_llaves):
    llavero = []
    for llav in arr_llaves:
        existe = False
        for rev in llavero:
            if llav == rev[0]:
                existe = True
                rev[1] += 1
                break
        if not (existe):
            llavero.append([llav, 1])
    return llavero


def f_leer():
    entrada = input()
    arreglo = [int(s) for s in entrada.split()]
    n_llaves = arreglo[0]
    n_cofres = arreglo[1]
    entrada = input()
    arr_llaves = [int(s) for s in entrada.split()]
    llavero = f_leer_llaves(arr_llaves)
    cofreria = []
    for r in range(n_cofres):
        entrada = input()
        arreglo = [int(s) for s in entrada.split()]
        tipo = arreglo[0]
        n_laves = arreglo[1]
        if n_llaves == 0:
            llaves = []
        else:
            llaves = f_leer_llaves(arreglo[:2])
        cofre = Cofres(tipo, llaves)
        cofreria.append([cofre, r+1])
    return [cofreria, llavero]


cofre1 = Cofres(1)
cofre2 = Cofres(1,[[1,1],[3,1]])
cofre3 = Cofres(2)
cofre4 = Cofres(3, [[2,1]])
cofreria = [[cofre1, 1], [cofre2, 2], [cofre3, 3], [cofre4, 4]]
llavero = [[1,1]]
print(f_abrir(cofreria, llavero))
