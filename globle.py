#importando bibliotecas necessárias
from basededados import base_de_dados
from basededados import paises
import random
import math
from random import choice
from operator import itemgetter
from dados import EARTH_RADIUS



#importando funcoes a serem utilizadas

#para sortear o país

def sorteia_pais(dici):
    pais_sorteado = choice([k for k in dici.keys()])
    
    return pais_sorteado

#medir a distancia dos países

def haversine(r,phi1,lambda1,phi2,lambda2):
    dentro_raiz = (math.sin(math.radians((phi2-phi1)/2)))*2 + (math.cos(math.radians(phi1))*math.cos(math.radians(phi2))(math.sin(math.radians((lambda2-lambda1)/2)))**2)
    return 2*r*math.asin(math.sqrt(dentro_raiz))

#sorteia letra com restriçao

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

#pais na lista de paises

def esta_na_lista(pais, lista):
    if pais in [pais[0] for pais in lista]: 
        return True
    return False

#lista de tentativas em ordem 

def adiciona_em_ordem(pais, d, lista):
    lista.append([pais, d])
    return sorted(lista, key=itemgetter(1))



######### MERCADO DE DICAS #######

#opcao 1
def verifica_bandeira(base_de_dados,pais):
    import random 
    lista =[]
    for cor,valor in base_de_dados[pais]['bandeira'].items():
        if valor != 0:
            lista.append(cor)
            cor_dica = random.choice(lista)
        return cor_dica

#opcao 2
def palavra_capital(base_de_dados,pais):
    for palavra in base_de_dados[pais]['capital']:
        
        letra = base_de_dados[pais]['capital'][0]  
    
    return letra

#opcao 3
def area(base_de_dados,pais):
    for area in base_de_dados[pais]['area']:
        area = base_de_dados[pais]['area']
    return area

#opcao 4

def pop(base_de_dados,pais):
    for populacao in base_de_dados[pais]['populacao']:
        populacao = base_de_dados[pais]['populacao']
    return populacao

#opcao 5

def continente (base_de_dados,pais):
    for cont in base_de_dados[pais]['continue']:
        cont = base_de_dados[pais]['continue']
    return cont