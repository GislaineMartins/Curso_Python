"""
Faça um programa que calcule a soma entre todos os números impares que são multiplos de tres e que
se encontram no intervalo de 1 até 500
"""
soma = 0

print('Soma de todos os número impares e multiplos de 3. No intervalo de 1 até 50')
for i in range(1,501):
    if i % 2 == 1 and i % 3 == 0:
        soma += i
        print(i)

