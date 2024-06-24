"""
Escreva um programa que leia um número inteiro qualquer e peça para
o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""

numero = int(input('Escreva um numero inteiro: '))

print(""" Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
""")
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINARIO é igal a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igal a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igal a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida. Tente novamente')

