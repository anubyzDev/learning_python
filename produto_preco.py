#076 Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.

#No final, mostre uma listagem de preços organizando os dados em forma tabular

escritorio = ('Mesam em L', 1490.00, 
'Teclado Mecânico', 1375.00, 
'Cadeira de Escritório', 1190.90, 
'Mouse Pad', 235.00, 
'Kuba Disco 2.0 Pro', 869.00)

print('='*40)
print(f'{"anubyzDev Workspace":^40}')
print('='*40)

for i in range(0, len(escritorio)):
    if i % 2 == 0:
        print(f'{escritorio[i]:.<30}',end='')
    else:
        print(f'R$ {escritorio[i]:>7.2f}')