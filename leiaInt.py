#104 Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenar um valor numérico

#Ex n = leiaInt()

def leiaInt(variavel):
    '''
    Funciona semelhante à Função Imput()
    '''
    
    while True:
        valor = input(variavel)
        if valor == '':
            print('\033[4;31mValor Indefinido!\033[m')
        else:
            if valor.isnumeric():
                valor = int(valor)
                break
            else:
                break
    return valor

            
            

teste = leiaInt('Digite algo: ')
print(f'Você digitou {teste}')
print(type(teste))
