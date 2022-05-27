#Anotações da aula de Função Parte 2

'''DOCSTRINGS

Basicmaente é uma string de documentação'''

from re import A


def soma(a=0, b=0, c=0):
    """
    Tutorial
    A FUnção Realiza a Soma entre os itens 'Inputados'
    """
    s = a + b + c
    return s

def teste(b):
    """
    Olhe bem para a função até entender o conceito de escopo global e local
    """
    global a
    a = 8
    b += 4
    c = 2
    print(f'a dentro valoe {a}')
    print(f'b dentro vale {b}')
    print(f'c dentro vale {c}')

r1 = soma(165, 27,)


a = 5
print(f'a antes do tratamento vale {a}')
teste(a)
print(f'a fora vale {a}')
print(f'A soma vale {r1}')