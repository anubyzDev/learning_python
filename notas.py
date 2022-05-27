#105 Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

'''
Quantidade de notas
A maior Nota
A Menor Nota
A média da Turma
A Situação (opcional) = Se vai passar SIM ou NÃO

Adicione também uma DOCSTRING à função
'''

from time import sleep

def titulo(title):
    tamanho = len(title)
    print('=' * (tamanho + 2))
    print(f' {title}')
    print('=' * (tamanho + 2))
    


def notas(nome, prova1, prova2, situaçao='<indefinido>'):
    '''
    Definir DOCSTRING*
    '''
    list_aluno = list()
    media = (prova1 + prova2) / 2

    if 7 > media <= 5:
        situaçao = 'Recuperação'
    elif media >= 7:
        situaçao = 'Aprovado'
    else:
        situaçao = 'Reprovado'

    dic_aluno = {nome, prova1, prova2, situaçao}
    list_aluno.append(dic_aluno.copy())
    dic_aluno.clear()

    return list_aluno



while True:
    decisao = str(input('Deseja cadastrar um aluno? [S/N] ')).strip().lower()[0]
    if decisao == 's':
        n = str(input('Digite um nome: '))
        p1 = float(input('Nota da Primeira Prova: '))
        p2 = float(input('Nota da Segunda Prova: '))
        notas(n, p1, p2)
        break
    elif decisao == 'n':
        print('Desconectando do Servidor...')
        sleep(1)
        break
    else:
        print('\033[31mOpção Inválida!\033[m')


print(notas())