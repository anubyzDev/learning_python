#078 Faça um programa que leia 5 valores e guarde-os em uma lista

#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
lista = []
for i in range(0,5):
    lista.append(int(input('Digite um inteiro: ')))
print(f'Essa é sua lista completa {lista}')
print(f'Esse é o maior termo da lista {max(lista)}')
print(f'Esse é o menor termo da lista {min(lista)}')