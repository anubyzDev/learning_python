#Anotações sobre a aula de Dicionários em Python

dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados)
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
print(dados)
print(dados['sexo'])
del dados['nome']
print(dados)

dota2 = {'Hero':'jakiro',
'Role':'Supp4',
'Type':'Damage per second'
}

print(dota2)
print(dota2['Hero'])
print(dota2['Role'])
print(dota2['Type'])

print(dota2.values()) #Valor
print(dota2.keys()) #Chave
print(dota2.items()) #Valor e Chave

for k,v in dota2.items(): #Lê-se por "O tipo é valor/ O key é vallue"
    print(f'o {k} é {v}')