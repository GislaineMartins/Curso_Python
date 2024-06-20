"""
Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salario do comprador
em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder
30% do salario ou então o emprestimo será negado
"""

valor_casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salario: '))
anos_pagamento = int(input('Em quanto anos vai pagar: '))

anos_em_meses = anos_pagamento * 12
limitacao_salario = salario * 0.3
valor_mnesalidade = valor_casa / anos_em_meses

if valor_mnesalidade < limitacao_salario:
    print('Emprestimo AUTORIZADO! ')
else:
    print('Emprestimo NEGADO! ')