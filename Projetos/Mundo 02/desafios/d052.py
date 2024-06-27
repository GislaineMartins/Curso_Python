"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número inteiro
"""

n = int(input('Digite um numero inteiro: '))
for i in range(1, n+1):
    if i.is_integer():
        print('{} é numero inteiro'.format(i))
    else:
        print('{} NÃO é numero inteiro'.format(i))