from random import randint
from time import sleep
from operator import itemgetter

print('o-'*25)
print(f'{"Dado em Casa": ^50}')
print('-o'*25)
print()
while True:
    dado = int(input('Modos de jogo\n[ 1 ] = D4\n[ 2 ] = D6\n[ 3 ] = D8\n[ 4 ] = D10\n[ 5 ] = D12\n[ 6 ] = D20\nSelecione um modo: '))
    if dado == 1:
        dado = 4
        break
    elif dado == 2:
        dado = 6
        break
    elif dado == 3:
        dado = 8
        break
    elif dado == 4:
        dado = 10
        break
    elif dado == 5:
        dado = 12
        break
    elif dado == 6:
        dado = 20
        break
    else:
        print('\033[4;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
jogo = {    'Jogador 1' : randint(1, dado),
            'Jogador 2' : randint(1, dado),
            'Jogador 3' : randint(1, dado),
            'Jogador 4' : randint(1, dado)}
vencedor = dict()

print('3...')
sleep(1)
print('2...')
sleep(1)
print('1...')
sleep(1)
print()

for k, v in jogo.items():
    print(f'O \033[32m{k}\033[m tirou \033[36m{v}\033[m')
    sleep(1)

vencedor = sorted(jogo.items(), key = itemgetter(1), reverse = True)
print('='*26)
print(f'{"Rank":<5} {"Jogador":<15} {"Pts":>2}')
for i, v in enumerate(vencedor):
    print(f'{i+1:<5} {v[0]:<15} {v[1]:>3}')
print('='*26)

#Dentro do sorted vc faz , key=itemgetter(1), reverse = True
#Dentro do sorted vc faz, key=itemgetter(1), reverse = True
#Completo fica vencedor = sorted(jogo.items(), key = itemgetter(1), reverse = True)