import random

def sorteia_letra(palavra,lista):
    especial = ['.', ',', '-', ';', ' ']
    final = []
    p = palavra.lower()
    for i in p:
        if i not in especial and i not in lista and i not in final:
            final.append(i)
    if final == []:
        return ""
    else:
        return (random.choice(final))