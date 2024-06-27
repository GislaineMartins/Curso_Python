"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores
obs: Maior idade = 21 anos
"""
from datetime import date
maiores_de_idade = 0
menores_de_idade = 0

for i in range(1,8):
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 21:
        menores_de_idade += 1
    else:
        maiores_de_idade += 1
print('Maiores de idade: {}'.format(maiores_de_idade))
print('Menores de idade: {}'.format(menores_de_idade))








