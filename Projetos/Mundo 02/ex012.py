"""
Aulas sobre laços de repetição
"""

for c in range(1,6):
    print('Oi')
print('FIM')

print('Segundo exemplo de FOR:')

for c in range(0,6):
    print(c)
print('FIM')

print('Terceiro exemplo de FOR:')

for c in range(6,0,-1):
    print(c)
print('FIM')

print('Quarto exemplo de FOR(pula de 2 em 2:')

for c in range(0,7,2):
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(0,n+1):
    print(c)
print('FIM')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')

print('Mais exemplos usando for: ')

s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {:.f}'.format(s))

