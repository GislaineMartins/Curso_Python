"""
11 -Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a
# quantidade de tinta necessaria para pinta-la, sabendo que cada litro da tinta pinta uma
# area de 2m^2
"""

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print(f'área: {area} metros quadrados')
qtdTinta = int(area/2)
print(f'{qtdTinta} litros')


