#072 Crie um Programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte

#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrálo por extenso

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

n = int(input('Digite um número de 0 até 20: '))

while n > 20 or n < 0:
    n = int(input('Digite um número de \033[32m0 até 20\033[m: '))
print(f'O valor digitado por extenso é {extenso[n]}')
