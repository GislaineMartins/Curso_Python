"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento.

Seu programa tambem deverá mostrar o tempo que falta  ou quanto tempo
passou do prazo
"""
from datetime import date

ano_nascimento = int(input('Informe o ano de nascimento: '))
ano_atual = date.today().year
subtracao_ano = ano_atual - ano_nascimento

if subtracao_ano < 18:
    print('Sua idade é {}.Você ainda vai se alistar ao serviço militar'.format(subtracao_ano))
elif subtracao_ano == 18:
    print('Sua idade é {}.Chegou a hora de alistar ao serviço militar'.format(subtracao_ano))
elif subtracao_ano > 18:
    print('Sua idade é {}.Já passou da hora de alistar ao serviço militar'.format(subtracao_ano))



