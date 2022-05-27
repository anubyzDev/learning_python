#100 Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar()

#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteadso pela função anterior

from random import randint

def sorteia(lista):
    for i in range(1, 6):
        lista.append(randint(0, 100))
    print(lista)
    print('-o' * 15)

def somaPar(funct):
    pares = 0
    for i in funct:
        if i % 2 == 0:
            pares += i
    print(f'A soma de todos os números pares é de {pares}')

numeros = list()
sorteia(numeros)
somaPar(numeros)
