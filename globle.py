#primeira funcao globle
def normaliza(continentes):
    normalizada = {}
    for continente, pais in continentes.items():
        try:
            for keys in pais.keys():
                normalizada[keys]=pais[keys]
                normalizada[keys]['continue'] = continente
        except: pass
    return normalizada
