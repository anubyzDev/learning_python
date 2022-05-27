#113 Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from entrada import leia


inteiro = leia.leiaInt('Digite um número inteiro: ')
real = leia.leiaReal('Digite um número real: ')

print(f'O valor do número inteiro foi {inteiro} e do número real foi {real}')
