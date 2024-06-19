"""
Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagem de até 200Km e R$0,45 para viagens mais longas.
"""

distancia = float(input('Digite a distancia de uma viagem em km: '))

if distancia <= 200:
    preco = distancia * 0.5
    print('Preço da passagem R${}'.format(preco))
else:
    preco = distancia * 0.45
    print('Preço da passagem R${}'.format(preco))