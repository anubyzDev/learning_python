#101 Escreva um programa que tenha uma função chamada voto() que vai recever como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÒRIO nas eleições


def voto(idade):
    from datetime import datetime
    nidade = datetime.now().year - idade
    if nidade < 18 and nidade >= 16 or nidade > 65:
        return f'Com {nidade} anos seu voto é \033[36mOpcional\033[m!'
    elif nidade >= 18 and nidade <= 65:
        return f'Com {nidade} anos seu voto é \033[32mObrigatório\033[m!'
    else:
        return f'Com {nidade} anos seu voto é \033[31mNegado\033[m!'

idade = int(input('Digite que ano você nasceu: '))
print(voto(idade))
    