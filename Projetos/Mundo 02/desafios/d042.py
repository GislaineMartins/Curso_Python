"""
Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar
que tipo de triangulo será formado:
- Equilatero: todos os lados iguais
- Isóceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
print('Digite os lados dos triangulos!')
primeiro_lado = float(input('Digite o lado 1:'))
segundo_lado = float(input('Digite o lado 2:'))
terceiro_lado = float(input('Digite o lado 3:'))

if primeiro_lado == segundo_lado and primeiro_lado == terceiro_lado and segundo_lado == terceiro_lado:
    print('Equilatero: todos os lados iguais')
elif primeiro_lado != segundo_lado and primeiro_lado != terceiro_lado and segundo_lado != terceiro_lado:
    print('Escaleno: todos os lados diferentes')
elif primeiro_lado == segundo_lado or primeiro_lado == terceiro_lado or segundo_lado == terceiro_lado:
    print('Isóceles: dois lados iguais')