#087 Aprimore a matriz mostrando agora:

#A) A soma de todos os valores pares digitados

#B) A soma dos valores da terceira coluna

#C) O maior valor da segunda linha

#0
#1
#2 0 1 2

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = terceira = comparar = 0

print('='*60)
print(f'\033[4;36m{"Matrinilizador":^60}\033[m')
print('='*60)

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor da posição [{l} {c}]: '))
        soma += matriz[l][c]
terceira = matriz[0][2] + matriz[1][2] + matriz[2][2]
for l in range(len(matriz)):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
for c in range(len(matriz)):
    if matriz[1][c] == 0:
        comparar = matriz[1][c]
    if matriz[1][c] > comparar:
        comparar = matriz[1][c]
print(f'A soma de todos os valores da matriz é \033[4;31m{soma}\033[m')
print(f'A soma dos valores da terceira coluna é \033[4;31m{terceira}\033[m')
print(f'O maior valor da segunda linha é \033[4;31m{comparar}\033[m')
