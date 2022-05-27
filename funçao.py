#Anotações da Aula de Funções do Python

#Basicamente a Função é um comando que você programou anteriormente e só chama ela

def l1():
    print('o-' * 15)


def l2():
    print('-o' * 15)


def mensagem(msg):
    print('-o' *15)
    print(f'{msg : ^30}')
    print('o-' *15)

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

l1()
print(f'{"Dota 2 Stats" : ^30}')
l2()

mensagem('Meta 7.31c')

#Drobrar Valores da Lista

dias = [5, 10, 15, 20]
print(dias)
dobra(dias)
print(dias)
