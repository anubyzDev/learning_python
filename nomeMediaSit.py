#090 Faça um programa que leia o nome e média de um aluno guardando também a situação em um dicionário

#No final mostre o conteudo da estrutura na tela

aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Situação'] = str(input('Digite a situação do aluno: '))
print(f'O aluno {aluno["Nome"]} está \033[36m{aluno["Situação"]}\033[m!')
