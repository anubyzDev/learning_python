#099 Faça um program,a que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.

#Seu programa tem que analisar todos os valores e dizer qual deles é o maior

#Desempacotamento

def maior(*num):
    cont = valor = maior = 0
    for valor in num:
        if cont == 0:
            maior = valor
            cont += 1
        else:
            if valor >= maior:
                maior = valor
        cont += 1
    print(f'O \033[32mmaior\033[m valor foi {maior}')
    print('-o' * 15)

maior(1, 3, 6, 7, 2, 15, 8)
maior(6)
maior(1, 8, 3, 27, 56, 46, 9)
maior()
