"""
Trabalhando com módulos ou bibliotecas e como utiliza-las no projetos. Nesse exemplo importa a
biblioteca math como exemplo
"""
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num) # raiz quadrada
print('A raiz de {} é igual a {}'.format(num, raiz))
# função math.ceil arredonda o valor pra cima
print('Valor de {} arredondado pra cima: {}'.format(raiz, math.ceil(raiz)))
# função math.floor arredonda o valor pra baixo
print('Valor de {} arredondado pra baixo: {}'.format(raiz, math.floor(raiz)))