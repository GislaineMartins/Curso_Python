"""
Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem
ou não formar um triangulo
"""

r1 = float(input('Digite o valor da reta 1: '))
r2 = float(input('Digite o valor da reta 2: '))
r3 = float(input('Digite o valor da reta 3: '))

soma = r1 + r2

if soma > r3:
    print('Os valores acima PODEM TRIANGULO!')
else:
    print('Os valores acima NÃO PODEM TRIANGULO!')