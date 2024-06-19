"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triangulo retangulo, calcule e mostre o comprimento da hipotenusa
"""
import math
cat_oposto = float(input('Digite o valor da cateto oposto: '))
cat_adjacente = float(input('Digite o valor da cateto adjacente:'))


# para achar a raiz math.sqrt()
cat_oposto_quadrado = math.pow(cat_oposto,2)
cat_adjacente_quadrado = math.pow(cat_adjacente,2)
hipotenusa = math.sqrt(cat_oposto_quadrado + cat_adjacente_quadrado)
print('Hipotenusa {:.2f}'.format(hipotenusa))



