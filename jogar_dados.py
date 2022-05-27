#091 Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatóros. Guarde esses resultados em um dicionário

#No final coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número no dado

from random import randint
from time import sleep
from operator import itemgetter

jogo = {    'Jogador 1' : randint(1, 6),
            'Jogador 2' : randint(1, 6),
            'Jogador 3' : randint(1, 6),
            'Jogador 4' : randint(1, 6)}
ranking = dict()
print('Valendo!')
sleep(1)
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse= True)
print(f'\033[32m{ranking}\033[m')
for k, v in enumerate(ranking):
    print(f'O {v[0]} ficou em {k+1}° lugar com {v[1]} no dado')
