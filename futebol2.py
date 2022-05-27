#095 Aprimore o desafio "futebol.py" para que funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

from time import sleep
from operator import itemgetter

jogadores_dict = dict()
jogadores_list = list()
gols = list()
aprov = cont = 0

print('-o'*20)
print(f'\033[36m{"ATACANTES" : ^40}\033[m')
print('o-'*20)

jogadores_dict['Nome'] = str(input('Cadastre um jogador: ')).strip().title()
jogadores_dict['Partidas'] = int(input('Cadastre a quantidade de partidas jogadas no campeonato: '))
for i in range(0, jogadores_dict['Partidas']):
    gol = (int(input(f'Quantidad de gols feito na partida {i+1}: ')))
    gols.append(gol)
    if gol > 0:
        cont += 1
jogadores_dict['Saldo de gols'] = gols[:]
jogadores_dict['Total de gols'] = sum(gols)
jogadores_dict['Aproveitamento'] = (cont / jogadores_dict['Partidas']) * 100
jogadores_list.append(jogadores_dict.copy())
gols.clear()
cont = 0
while True:
    continuar = str(input('Deseja cadastrar outro jogador? [S/N] ')).strip().lower()
    if continuar == 's':
        jogadores_dict['Nome'] = str(input('Cadastre um jogador: ')).strip().title()
        jogadores_dict['Partidas'] = int(input('Cadastre a quantidade de partidas jogadas no campeonato: '))
        for i in range(0, jogadores_dict['Partidas']):
            gol = int(input(f'Quantidade de gols feito na partida {i+1}: '))
            gols.append(gol)
            if gol > 0:
                cont += 1
        jogadores_dict['Saldo de gols'] = gols[:]
        jogadores_dict['Total de gols'] = sum(gols)
        jogadores_dict['Aproveitamento'] = (cont / jogadores_dict['Partidas']) * 100
        jogadores_list.append(jogadores_dict.copy())
        gols.clear()
    elif continuar == 'n':
        print('Encerrando Software...')
        sleep(1)
        break
    else:
        print('\033[4;31mOPÇÃO INVÁLIDA!\033[m')

for i, v in enumerate(jogadores_list):
    print(f'O valor de {i} é {v}')
print(jogadores_list)
print(jogadores_dict)
