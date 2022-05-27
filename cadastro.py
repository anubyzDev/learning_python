#094 Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada um em um dict

#Guarde todos os dicionários em uma lista, No final mostre:

#A)Quantas pessoas foram cadastradas CHECK
#B)A média de idade do grupo CHECK
#C)Uma lista com todas as mulheres CHECK
#D)Uma lista com todas as pessoas com idade acima da média
from datetime import datetime
from time import sleep

continuar = 's'
cadastro = dict()
listagem = list()
contagem_mulher = idade_media = 0
listagem_mulher = list()
velho = list()

while True:
    if continuar == 'n':
        print('Finalizando Software...')
        sleep(1)
        break
    else:
        cadastro['Nome'] = str(input('Cadastre o nome: ')).strip().title()
        cadastro['Sexo'] = str(input('Qual o sexo? [M/F] ')).strip().lower()
        if cadastro['Sexo'] == 'f':
            contagem_mulher += 1
            listagem_mulher.append(cadastro['Nome'])
        nasc = int(input('Digite o ano de nascimento: '))
        cadastro['Idade'] = datetime.now().year - nasc
        idade_media += cadastro['Idade']
        listagem.append(cadastro.copy())
        cadastro.clear()
        continuar = str(input('Deseja cadastrar uma nova pessoa? [S/N] ')).strip().lower()
        if continuar == 's':
            print('Iniciando novo cadastro...')
            sleep(1)
        elif continuar == 'n':
            print('Finalizando Software...')
            sleep(1)
            break
        else:
            while True:
                if continuar == 's':
                    print('Iniciando novo cadastro...')
                    sleep(1)
                    break
                elif continuar == 'n':
                    break
                else:
                    continuar = str(input('\033[4;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE! [S/N] \033[m'))

for i, v in enumerate(listagem):
    print(f' {i} {v}')
    if (listagem[i]['Idade']) > (idade_media/len(listagem)):
        velho.append(listagem[i]['Nome'])
    #if listagem[i]['Idade'] > (idade_media/len(listagem)):
        #velho.append(listagem['Idade'])
print(listagem[0]['Nome'])
print(f'Foram cadastradas {len(listagem)} pessoas, sendo {contagem_mulher} pessoa(s) mulher')
print(listagem_mulher)
print(f'A média de idade do grupo é de {idade_media/len(listagem) :.0f} anos')
print(f'As pessoas acima da média de idade são {velho}')