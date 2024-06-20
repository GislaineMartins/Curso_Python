"""
Escreva um programa que leia um número inteiro qualquer e peça para
o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""

numero = int(input('Escreva um numero inteiro de 1 a 3: '))

if numero == 1:
    print('Conversao para binario!')
elif numero == 2:
    print('Conversao para octal!')
elif numero == 3:
    print('Conversao para hexadecimal!')
