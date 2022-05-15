def esta_na_lista(pais, lista):
    if pais in [pais[0] for pais in lista]: 
        return True
    return False