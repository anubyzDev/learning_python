#102 Escreva um programa que fata o Fatorial de um número em forma de função e também mostre o passo a passo com show=True

def fatorial(num, show=False):
    f = 1
    for i in range(num, 0, -1):
        if show:
            print(f'{i} ', end='')
            if i > 1:
                print('x ', end='')
            else:
                print('= ', end='')
        f *= i
    return f

n1 = 5
f1 = fatorial(n1)
n2 = 6
f2 = fatorial(n2)

print(f'O fatorial de {n1} é {fatorial(n1)}')
print(f'O fatorial de {n2} é {fatorial(n2)}')

while True:
    decisao = str(input('Deseja ver a resolução do exercício? [S/N] ')).strip().upper()[0]
    if decisao == 'S':
        print(fatorial(n1, show=True))
        break
    elif decisao == 'N':
        break
    else:
        print('\033[31mOpção inválida!\033[m')

