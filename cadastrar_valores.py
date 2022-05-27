#079 Crie um programa que leia varios valores e os cadastre em uma lista,caso o valor já exista na lista ele não é cadastrado

#No fim da execução serão exibidos todos os valores únicos cadastrados em ordem crescente

lista = []

lista.append(int(input('Cadastre um valor na lista: ')))
while True:
    continuar = str(input('Deseja cadastrar outro valor na lista [S/N]? ')).strip().lower()
    if continuar == 's':
        valor = int(input('Adicione um novo valor: '))
        if valor in lista:
            print('\033[31mValor já cadastrado\033[m')
        else:
            lista.append(valor)
    elif continuar == 'n':
        break
    else:
        print('\033[31mOpção inválida!\033[m')
print(lista)