#081 Crie um programa que leia vários números e os adicione em uma lista, depois disso mostre:

#A)Quantos números foram digitados
#B)A lista de valores ordenada de  forma decrescente
#C)Se o valor 5 foi digitado e está ou não na lista
 
lista = []

lista.append(int(input('Adicione um valor à lista: ')))
while True:
    deseja = str(input('Deseja adicionar um novo valor? [S/N] ')).strip()
    if deseja == 'n' or deseja == 'N':
        break
    elif deseja == 's' or deseja == 'S':
        lista.append(int(input('Informe mais outro valor: ')))
    else:
        print('Opção inválida!')
print(f'Foram adicionados \033[32m{len(lista)}\033[m valores')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')
if lista.count(5) > 0:
    print(f'O valor 5 foi digitado {lista.count(5)} vezes')
else:
    print('O valor 5 \033[31mnão\033[m está na lista!')