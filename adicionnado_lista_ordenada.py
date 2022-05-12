from operator import itemgetter
def adiciona_em_ordem(pais, d, lista):
    lista.append([pais, d])
    return sorted(lista, key=itemgetter(1))