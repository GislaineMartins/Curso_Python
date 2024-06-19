"""
Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente
desse angulo
"""
"""
math.degrees(x)
Converte radianos para graus

math.radians(x)
Converte o angulo de graus para radianos.
"""
import math
angulo = int(input('Digite o angulo: '))
valor_radiano = math.radians(angulo)
cosseno = math.cos(valor_radiano)
seno = math.sin(valor_radiano)
tangente = math.ceil(math.tan(valor_radiano))

print('O cosseno de {} é {}: '.format(angulo, cosseno))
print('O seno de {} é {}: '.format(angulo, seno))
print('A tangente de {} é {}: '.format(angulo, tangente))



