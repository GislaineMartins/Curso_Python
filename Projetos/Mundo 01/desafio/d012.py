#12 - Faça um algortimo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto

preco_produto = float(input('Digite o preço do produto: '))

desconto = preco_produto* 0.05
novo_preco = preco_produto - desconto

print('Valor com desconto R${:.2f}'.format(novo_preco))