#089 Crie um programa que leia o nome e duas notas de vários alunos em uma lista composta e no final mostre:

#Boletim mostrando a média de cada aluno e permita que o programa mostre a nota de cada aluno individualmente

aluno = list()
dados = [[], [], [], []]

dados[0] = str(input('Cadastre um aluno: ')) #Nome do aluno
dados[1] = float(input('Nota da primeira prova: ')) #Nota da primeira prova
dados[2] = float(input('Nota da segunda prova: ')) #Nota da segunda prova
dados[3] = (dados[1] + dados[2]) / 2 #Nota Final
aluno.append(dados[:])
dados.clear()

while True:
    novo_cadastro = str(input('Deseja adicionar um novo aluno? [S/N]: ')).strip().upper()
    if novo_cadastro == 'N':
        break
    elif novo_cadastro == 'S':
        dados = [[], [], [], []]
        dados[0] = str(input('Cadastre um aluno: '))
        dados[1] = float(input('Nota da primeira prova: '))
        dados[2] = float(input('Nota da segunda prova: '))
        dados[3] = (dados[1] + dados[2]) / 2
        aluno.append(dados[:])
        dados.clear()
    else:
        print('\033[31mOPÇÃO INVÁLIDA!\033[m')
print('='*32)
print(f'{"♦":<5} {"Nome":<10} {"Média":>15}')
for i in range(0, len(aluno)):
    print(f'{i:<5} {aluno[i][0]:<10} {aluno[i][3]:>15}')
print('='*32)
while True:
    separado = int(input('Veja as notas do aluno separadamente [Digite 999 para finalizar]: '))
    if separado == 999:
        break
    else:
        print(f'{aluno[separado][0]}: A nota da P1 foi: {aluno[separado][1]}')
        print(f'{aluno[separado][0]}: A nota da P2 foi: {aluno[separado][2]}')
