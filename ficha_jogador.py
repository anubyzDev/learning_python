#103 Faça um programa que tenha uma função chamada ficha(), que receba dois paâmetros opcionais: o nome de um jogador e quantos gols ele marcou

#O programa deverá ser capaz de mostra a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(nome='<<< desconhecido >>>', gols=0):
    '''
    Função: ficha(nome='<<< desconhecido >>>'\ gols=0)
    nome --> Nome do Jogador
    gols -- Quantidade de Gols na Partida

    Retorna Ficha de Nome do Jogador com Quantidade de Gols cadastrados
    '''
    return f'O jogador {nome} fez {gols} gol(s)'

n = str(input('Digite o nome do jogador: ')).strip().title()
g = str(input('Quantidade de gols feitos pelo jogador: '))
if n == '':
    if g.isnumeric():
        g = int(g)
        print(ficha(gols=g))
    else:
        print(ficha())
else:
    if g.isnumeric():
        g = int(g)
        print(ficha(n, g))
    else:
        print(ficha(n))
