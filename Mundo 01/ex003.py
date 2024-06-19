
"""
Aula teorica sobre valores primitivos - PARTE 01
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro:'))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1,n2,s))
"""
#*********************************************************************
"""
# Aula teorica sobre valores primitivos - PARTE 02
n = float(input('Digite um valor: '))
print(n)
print(type(n))
"""
#*********************************************************************
"""
# Aula teorica sobre valores primitivos - PARTE 03
n = input('Digite algo: ')
# Função para identificar se o que foi digitado é alfanumerico (retorno: true ou false)
print(n.isalnum())
# Função para identificar se o que foi digitado esta em maiusculo (retorno: true ou false)
print(n.isupper())
"""
# Crie um programa que leia dois numeros e mostre a soma entre eles
print('EXERCICIO 01')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre {} e {} é {}'.format(n1,n2,s))

# Crie um programa que leia dois numeros e mostre a soma entre eles
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.
print('EXERCICIO 02')
n = input('Digite algo: ')

# Garante que uma string contém apenas caracteres ASCII
print(n.isascii())
# Garante que uma entrada do usuário contém apenas caracteres alfabético
print(n.isalpha())
# Garante que uma string está em maiúsculas
print(n.isupper())
# Verifica se todos os caracteres de uma string são dígitos decimais (0-9)
print(n.isdigit())
# Verifica se todos os caracteres de uma string são caracteres decimais
print(n.isdecimal())
# Identificadores são nomes usados para definir variáveis, funções, classes, módulos e outros objetos no código Python
print(n.isidentifier())
# Verifica se todos os caracteres alfabéticos em uma string estão em letras minúsculas
print(n.islower())
# Verifica se todos os caracteres de uma string são caracteres numéricos
# Verifica tambem se a string não esta vazia
print(n.isnumeric())
#  verificar se todos os caracteres de uma string são caracteres imprimíveis
#  Caracteres imprimíveis incluem letras, dígitos, pontuação, espaços e símbolos, basicamente todos os caracteres que
#  podem ser exibidos na tela
print(n.isprintable())
# verificar se todos os caracteres de uma string são espaços em branco
# Caracteres de espaço em branco incluem espaços, tabulações (\t), novas linhas (\n), retornos de carro (\r)
print(n.isspace())
# verificar se uma string está em formato de título
print(n.istitle())










