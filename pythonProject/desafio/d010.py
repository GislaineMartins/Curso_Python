# 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares
# dolares ela pode comprar. Considere US$1,00 = R$3,27

n = float(input('Digite um valor em reais. R$'))
dolares = n/3.27
print('Voce pode comprar US${:.2f}'.format(dolares))