"""
Escreva um programa que faça o computador 'pensar' em um número inteiro
entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número
escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu
"""
import random

numero_usuario = int(input('Digete um número entre 0 e 5: '))
valor = int(random.randint(1,5))

if numero_usuario == valor:
    print('Voce venceu! Número digitado {} numero gerado pelo computador {}'.format(numero_usuario, valor))
else:
    print('Voce perdeu! Número digitado {} numero gerado pelo computador {}'.format(numero_usuario, valor))

