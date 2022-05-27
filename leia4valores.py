#075 Desenvolva um programa que leia 4 valores e depois os guarde em uma tupla. No final, mostre;

#A)Quantas vezes apareceu o valor 9
#B) Em que posição foi digitado o primeiro valor 3
#Quais foram os números pares
n_tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))

print(f'O número "9" aparece {n_tupla.count(9)} veze(s)')
if 3 in n_tupla:
    print(f'O número "3" aparece na posição {n_tupla.index(3)} da tupla')
else:
    print('O valor "3" não foi digitado  em nenhuma posição')
print(f'Os números pares foram: ', end='')
for n in n_tupla:
    if n % 2 == 0:
        print(n,end=' ')