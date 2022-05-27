#098 Faça um programa que tgenha uma função chamada contador(), que receba três parâmetros: Início, fmi e passo e realize a comtagem

#Seu programa tem que realizar três contagens através da função criada:

'''
A) De 1 até 10, de 1 em 1 Check
B) de 10 até 0, de 2 em 2
C)Uma Contagem Personalizada'''
from time import sleep

def contador(inicio, final, passo):
    if passo > 0:
        if inicio <= final:
            while inicio <= final:
                print(inicio, end=' ')
                sleep(1)
                inicio += passo
            print('FIM')
        else:
            while final <= inicio:
                print(inicio, end=' ')
                sleep(1)
                inicio -= passo
            print('FIM')
    elif passo == 0:
        print('Faça me o favor, né amigo...')
    else:
        while final <= inicio:
            print(inicio, end=' ')
            sleep(1)
            inicio += passo
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Digite o Inicio da contagem: '))
f = int(input('Digite o Final da contagem: '))
p = int(input('Digite o intervalo da contagem: '))
contador(i, f, p)