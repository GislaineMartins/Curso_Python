"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- A vista (dinheiro/pix): 10% de desconto
- A vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

valor_produto = float(input('Digite o valor do produto: '))
print('Digite 1 para pagamento em (dinheiro/pix): ')
print('Digite 2 para pagamento vista no cartão: ')
print('Digite 3 para pagamento em até 2x no cartão: ')
print('Digite 4 para pagamento 3x ou mais no cartão: ')
opcao = int(input('Digite a opcao: '))

if opcao == 1:
    novo_valor = valor_produto - (valor_produto * 0.10)
    print('10% de desconto. Valor R${}'.format(novo_valor))
elif opcao == 2:
    novo_valor = valor_produto - (valor_produto * 0.05)
    print('5% de desconto. Valor R${}'.format(novo_valor))
elif opcao == 3:
    print('Não possui desconto. Valor R${}'.format(valor_produto))
elif opcao == 4:
    novo_valor = valor_produto + (valor_produto * 0.20)
    totParc = int(input('Quantas parcelas? '))
    parcela = novo_valor / totParc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totParc, parcela))
    print('Não possui desconto. Valor R${}'.format(novo_valor))
else:
    print('Opção invalida!')

