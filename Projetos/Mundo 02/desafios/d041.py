"""
A confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com
a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SENIOR
- Acima de 20 anos: MASTER
"""
from datetime import date

ano_nascimento = int(input('Digite o ano em que nasceu: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Voce tem {} anos. Categoria: MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('Voce tem {} anos. Categoria: INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
    print('Voce tem {} anos. Categoria: JUNIOR'.format(idade))
elif idade > 19 and idade <= 20:
    print('Voce tem {} anos. Categoria: SENIOR'.format(idade))
else:
    print('Voce tem {} anos. Categoria: MASTER'.format(idade))



