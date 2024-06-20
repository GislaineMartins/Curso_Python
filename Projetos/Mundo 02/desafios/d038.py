"""
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

if numero1 > numero2:
    print('Numero {} é maior.'.format(numero1))
elif numero2 > numero1:
    print('Numero {} é maior.'.format(numero2))
elif numero2 == numero1:
    print('Numero {} e Numero {} são iguais.'.format(numero1, numero2))