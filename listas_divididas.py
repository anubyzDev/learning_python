#082 Crie um programa que leia vários valores e coloque em uma lista

#Crie duas outras listas para mostrar os valores ímpares e pares separadamente em cada uma das listas
#No final mostre as 3 listas geradas

lista = []
par = []
impar = []

lista.append(int(input('Adicione um valor à lista: ')))
while True:
    deseja = str(input('Deseja adicionar outro valor? [S/N] ')).strip().lower()
    if deseja == 'n':
        break
    elif deseja == 's':
        valor = int(input('Digiet um novo valor: '))
        lista.append(valor)
        if valor % 2 == 0:
            par.append(valor)
        else:
            impar.append(valor)
    else:
        print('\033[32mOpção Inválida!\033[m')
print(f'Sua lista de números inteiros é {lista}')
print(f'Sua lista com os números \033[36mpares\033[m é {par}')
print(f'Sua lista com os números \033[36mímpares\033[m é {impar}')
