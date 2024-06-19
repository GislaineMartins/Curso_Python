"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
"""
ano = int(input("Digite o ano: "))
dezena = ano // 10 % 10
unidade = ano // 1 % 10

conc_dezena = str(dezena)
conc_unidade = str(unidade)
numeros_concatenados = conc_dezena + conc_unidade

numeros_finais = int(numeros_concatenados)

if numeros_finais % 2 == 0:
    print('{} é BISSEXTO!'.format(ano))
else:
    print('{} NÃO é BISSEXTO!'.format(ano))












