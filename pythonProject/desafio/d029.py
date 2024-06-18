"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/k, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite
"""
velocidade = float(input('Digite a velocidade do carro: '))

if velocidade > 80:
    valor_multa = (velocidade - 80) * 7
    print('Voce foi multado no valor de {}'.format(valor_multa))
else:
    print('Não possui multa')