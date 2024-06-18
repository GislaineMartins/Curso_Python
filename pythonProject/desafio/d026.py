"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a ultima vez
"""

frase = str(input('Digite uma frase: ')).upper().strip()
print('Quantidade de vezes que aparece a letra a: ', frase.count('A'))
print('Posição que ela aparece a primeira vez: ', frase.find('A')+1)
print('Posição que ela aparece a ultima vez: ', frase.rfind('A')+1)



