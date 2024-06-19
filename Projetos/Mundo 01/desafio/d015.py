"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por
dia e R$0,15 por Km rodado
"""
qtd_percorrida = float(input('Digite a quantidade de Km que o carro percorreu: '))
dias_alugados = int(input('Digite a quantidade de dias alugado: '))

custo_por_dia = dias_alugados * 60
custo_km = qtd_percorrida * 0.15
custo_total = custo_por_dia + custo_km

print('Valor total R${}'.format(custo_total))
