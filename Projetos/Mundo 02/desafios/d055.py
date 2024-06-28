"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor
peso lidos.
"""

menor_peso = 0
maior_peso = 0
anterior = 0

for p in range(1,6):
    print('Digite peso {}: '.format(p))
    peso = float(input())

    if p == 1:
        maior_peso = peso
        menor_peso = peso
    elif peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso


print("Maior peso: {}".format(maior_peso))
print("Menor peso: {}".format(menor_peso))

