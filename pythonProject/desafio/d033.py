"""
Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor
"""

n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
n3 = int(input('Digite o número 3: '))

# Verficando quem é o menor
menor = n1

if n2 < n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
# Verficando quem é o maior
maior = n1

if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))


