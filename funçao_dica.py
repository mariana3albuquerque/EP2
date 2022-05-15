tentativas = 20
palpite = input('qual o país? você tem {} tentativas'.format(tentativas))

def dica(opcao):

    if opcao == '0':
        return palpite
    if opcao == '1' and tentativas > 4:
        print(verifica_bandeira(base_de_dados,pais_sorteado))
        tentativas -= 4
        return palpite

    if opcao == '2' and tentativas > 3:
        print(palavra_capital(base_de_dados,pais_sorteado))
        tentativas -= 3
        return palpite
    if opcao == '3' and tentativas > 6:
        print(area(base_de_dados,pais_sorteado))
        tentativas -= 6
        return palpite
    if opcao == '4' and tentativas > 5:
        print(pop(base_de_dados, pais_sorteado))
        tentativas -= 5
        return palpite
    if opcao == '5' and tentativas > 7:
        print(continente(base_de_dados,pais_sorteado))
        tentativas -= 7
        return palpite