#092 Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um  dicionário

#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salario

#Calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar

from datetime import datetime

dados = dict()
dados['Nome'] = str(input('Cadastre um nome: ')).strip().capitalize()
nasc = int(input('Cadastre o ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Cadastre sua carteira de trabalho [Digite 0 se não tiver] '))

if dados['ctps'] != 0:
    dados['Contratação'] = int(input('Informe o ano de contratação: '))
    dados['Salário'] = float(input('Informe o salário: '))
    dados['Aposentadoria'] = (dados['Contratação'] + 35) - nasc
print(dados)