#093 Crie um programa que gerencie o aproveitamento de um jogador de futebol

#O programa deve ler o nome e quantas partidas ele jogou, depois vai ler a quantidade de gols feitos em cada partida

#No final o programa deverá mostrar tudo com a quantidade de gols feitos no campeonato

jogador = {'Nome' : str(input('Digite o nome do jogador: ')), 'Partidas' : int(input('Quantidade de partidas no campeonato: '))}
gol_total = aproveitamento = aprov = 0
print(f'O jogador {jogador["Nome"]} tem {jogador["Partidas"]} partidas no campeonato')

for i in range(1, jogador['Partidas']+1):
    gol = (int(input(f'Digite quantos Gols o {jogador["Nome"]} fez na {i} partida: ')))
    if gol > 0:
        aprov += 1
    gol_total += gol
aproveitamento = (aprov/jogador['Partidas']) * 100
print(f'{jogador["Nome"]} fez um total de {gol_total}')
print(f'Aproveitamento de {aproveitamento:.1f} %')