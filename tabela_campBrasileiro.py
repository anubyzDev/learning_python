#073 Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre

#A)Apenas os 5 Primeiros Colocados.
#B)Os últimos 4 colocados da tabela.
#C)Uma lista com os times em orgem alfabética.
#D)Em que posição na tabela está o time da Chapecoense.

br = ('São Paulo', 'Coritiba', 'Corinthians', 'Atlético Mineiro', 
'Ceará', 'Avaí', 'Cuiba', 'Juventus', 
'Red Bull Bragantino', 'Flamengo', 'Atlético', 
'Santos', 'Fluminense', 'Palmeiras', 'Fortaleza', 
'Amperica Fc Sal', 'Botafogo', 'Internacional', 'Goiás', 'Athletico Paranaense')

print('Os 5 primeiro colocados são:')
for c in range(0, 5):
    print(f'{br[c]}')
print('Os 4 últimos colocados em zona de rebaixamento são:')
for c in range(16, 20):
    print(br[c])
print('Assim é a lista de times em ordem alfabética:')
ordenado = sorted(br)
for c in range(0, 20):
    print(ordenado[c])
print(f'O Palmeiras está na {br.index("Palmeiras")+1}° posição')
