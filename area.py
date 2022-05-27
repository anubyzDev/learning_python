#096 Faça um programa para calcular área de um terreno

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área do terreno é de {area} m²')

largura = float(input('Digite a \033[32mLargura\033[m do terreno: '))
comprimento = float(input('Digite o \033[32mComprimento\033[m do terreno: '))

area(largura, comprimento)