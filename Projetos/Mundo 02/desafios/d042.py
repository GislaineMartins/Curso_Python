"""
Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar
que tipo de triangulo será formado:
- Equilatero: todos os lados iguais
- Isóceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triangulo', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triangulo')