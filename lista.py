print(f'{"Hero Pool Supports":=^80}')

hero_pool = ['Jakiro', 'Rubick', 'Bane', 'Ogre Mage', 'Tusk']
print(hero_pool)
hero_pool[3] = 'Clockwork'
print(hero_pool)
hero_pool.append('Hoodwink')
print(hero_pool)
hero_pool.insert(1,'Lion')
print(hero_pool)
hero_pool.insert(0,'Furion')
print(hero_pool)

hero_pool.remove('Furion')
del hero_pool[6]
hero_pool.pop(2)

print('Minha Hero Pool Supports ordenada é: ')

for hero in range(0, len(hero_pool)):
    print(f'{hero+1}° {hero_pool[hero]}')

valores = list(range(4, 10))
valores.sort(reverse=True)
print(valores)

teste = [6, 1]
novo = [4]
final = teste + novo
print(final)