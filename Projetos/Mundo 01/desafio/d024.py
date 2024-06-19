"""
Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome "SANTO"
"""

cidade = input("Digite o nome de uma cidade: ")
letra_maiuscula = cidade.upper()

verificacao_palavra = letra_maiuscula.split()
print('A primeira palavra é: ',verificacao_palavra[0])



