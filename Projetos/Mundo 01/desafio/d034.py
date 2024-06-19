"""
Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
Para salarios superiores a R$1250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%
"""

salario = float(input('Digite o seu salario: '))

if salario > 1250.00:
    novo_salario = (salario * 0.10) + salario
    print('Seu novo salario é: {}'.format(novo_salario))
else:
    novo_salario = (salario * 0.15) + salario
    print('Seu novo salario é: {}'.format(novo_salario))