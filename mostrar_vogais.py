#077 Crie um programa que tenha uma tupla com várias palavras (sem acento), depois disso você deve mostrar para cada palavra quais são sua vogais

palavras = ('Cimento', 'Cadeira', 'Teclado', 'Joaninha', 'Esquilo', 'Simpatico')

for i in palavras:
    print(f'\nNa palavra {i.upper()} temos as vogais: ',end='')
    for vogais in i:
        if vogais.lower() in 'aeiou':
            print(f'{vogais.upper()}',end=' ')
