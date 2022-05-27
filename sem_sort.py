#080 Crie um programa onde o usuário possa digitar cinco valores numéricos  e cadastrá-los em uma lista já na posição correta de inserção (sem usar o sort)

#No final mostre a lista ordenada na tela

'''numeros = []

for i in range(0, 5):
    valor = int(input(f'Digite o {i+1}° valor: '))
    if i == 0:
        numeros.append(valor)
    else:
        if valor <= numeros[0]:
            numeros.insert(0, valor)
        if i == numeros [-1]:
            numeros.insert(valor, numeros[1])
        if valor > numeros[-1]:
            numeros.append(valor)
    pos = 0
    while pos < len(numeros):
print(numeros)'''