print('\033[31mVariáveis Compostas')
print('\033[4mTUPLAS\033[m')

#tuplas se parecem com variavel = ('item1', 'item2', 'item3')
c = 0
lanche = ('suco', 'pizza', 'dinossauro')
print(lanche)
print(lanche[2])
print(lanche[-2])
hero_pool = ('Jakiro', 'Clockwerk', 'Tuskar')
print('Essa é minha Tríplice Dotística para chegar ao Legend MMR')
for hero in hero_pool:
    c += 1
    print(f'Esse é o meu {c}° {hero} mais forte')

for hero in range(0, len(hero_pool)):
    print(f'Eu vou jogar de {hero_pool[hero]}')

for pos, hero in enumerate(hero_pool):
    print(f'{pos}° eu vou jogar de {hero}')

#Realiza testes com o comando sorted(var)

a = (1, 2, 3, 5, 7)
b = (4, 6, 8, 9)
c = b + a

print(c)
print(sorted(c))