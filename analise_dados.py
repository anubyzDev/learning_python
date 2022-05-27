#084 Faça um programa que leia o nome e peso de várias pessoas guardando tudo em uma lista.No final mostre

#A) Quantas pessoas foram cadastradas
#B) Uma listagem com as pessoas mais pesadas
#C) Uma listagem com as pessoas mais leves

pessoas = list()
composta = list()
comparar_pesado = 0
comparar_leve = 0
c = 0

composta.insert(0, (str(input('Cadastre uma pessoa: '))))
composta.insert(0, (int(input('Cadastre seu peso: '))))
pessoas.append(composta[:])
c += 1
while True:
    del composta[:]
    cadastro = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).strip().lower()
    if cadastro == 's':
        composta.insert(0, (str(input('Cadastre um nome: '))))
        composta.insert(0, (int(input('Cadastre seu peso: '))))
        pessoas.append(composta[:])
        composta.pop()
        c += 1
    elif cadastro == 'n':
        break
    else:
        print('\033[4;31mOpção Inválida!\033[m')
for i in range(0, len(pessoas), 2):

#print(pessoas)
#print(composta)
#print(f'Foram cadastradas {c} pessoas')