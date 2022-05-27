dota2 = {
    'supp5' : 'Jakiro',
    'supp4' : 'Shadow Demon',
    'roamming' : 'Clockwork',
    'Offlaner' : 'Night Stalker',
    'Hard Carrier' : 'Juggernout',
    'Mid Laner' : 'Natures Prophet'
}

print(dota2)
print(dota2['supp4'])
print(dota2['Hard Carrier'])

print('o-'*20)
for k, v in dota2.items():
    print(k)
print('-o'*20)
for k, v in dota2.items():
    print(v)