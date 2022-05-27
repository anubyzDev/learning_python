#085 Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.

#Mostre em listas separadas os valores pares e ímpares em ordem crescente

#O exercício deve ser composto por uma lista com duas listas internas

numeros = list()
par = list()
impar = list()

for i in range(0,7):
    numeros.append(int(input('Digite um número inteiro qualquer: ')))
    if numeros[0] % 2 == 0:
        par.append(numeros[0])
    if numeros[0] % 2 == 1:
        impar.append(numeros[0])
    numeros.clear()
numeros = par + impar
numeros.sort()
print(f'Partindo da lista ordenada {numeros}')
par.sort()
impar.sort()
print('Os números \033[32mpares\033[m digitados foram', end='')
for i in par:
    print(f' --> {i}', end='')
print('\nOs números \033[32mímpares\033[m digitados foram', end='')
for i in impar:
    print(f' --> {i}', end='')
print('\n')
