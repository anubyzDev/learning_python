#097 Escreva um programa com que print um texto com tamanho adaptável

def escreva(txt):
    tam = len(txt) + 2
    print(f'~' * tam)
    print(f' {txt}')
    print(f'~' * tam)


escreva('Olá, Mundo!')
escreva('Oi')
escreva('Cu de Gambá')