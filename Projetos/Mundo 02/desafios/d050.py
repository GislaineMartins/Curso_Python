"""
Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor for impar desconsidere
"""
soma = 0
print('Digite 6 numeros!')
for i in range(1,7):
    n = int(input('Digite numero {}: '.format(i)))
    if i % 2 == 0:
        soma += i
print('Soma de todos os numero pares {}'.format(soma))