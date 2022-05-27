#074 Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla

#Depois disso, mostre a listagem de números gerados e indique o menor e o maior valor que estão na tupla

from random import randint

numero = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(numero)
arrumado = sorted(numero)
print(arrumado)
print(f'O maior número é {arrumado[-1]}')
print(f'O menor número é {arrumado[0]}')

print(f'O maior número é {max(numero)}')
print(f'O menor número é {min(numero)}')