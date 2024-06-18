# 13- Faça um algortimo que leia o salario de um funcionario e mostre seu novo salario,
# com 15% de aumento

salario = float(input('Digite seu salario: '))
aumento = salario * 0.15
novo_salario = salario + aumento

print('Salario com desconto de 15%: R${:.2f}'.format(novo_salario))
