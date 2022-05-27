#086 Crie um programa que leia 9 valores e os mostre em forma de matriz 3x3

#No final do programa mostre a matriz com a formatação correta

#0
#1
#2
# 0 1 2

lin1 = [[], [], []]
lin2 = [[], [], []]
lin3 = [[], [], []]

print('\033[36mMatrizificador\033[m')

for i in range(0,3):
    valor = int(input(f'DIgite um valor para [0] [{i}] '))
    lin1[i].append(valor)
for i in range(0,3):
    valor = int(input(f'Digite um valor para [1] [{i}] '))
    lin2[i].append(valor)
for i in range(0,3):
    valor = int(input(f'Digite um valor para [2] [{i}] '))
    lin3[i].append(valor)

print(lin1)
print(lin2)
print(lin3)
