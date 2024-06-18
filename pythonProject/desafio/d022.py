"""
Crie um programa que leia o nome completo de uma pessoa e mostre
- O nome com todas as letras maiusculas
- O nome com todas as letras minusculas
- Quantas letras no total (sem considerar espaços)
- Quantas letras tem o primeiro nome
"""
nome = input('Digite seu nome completo: ')
print('Nome com todas as letras maiusculas: ',nome.upper())
print('Nome com todas as letras minusculas: ',nome.lower())
nome_sem_espaco = nome.replace(" ", "")
print('Quantidade de letras no total ',len(nome_sem_espaco))
primeiro_nome = nome.split()
print('Quantidade de letras do primeiro nome',len(primeiro_nome[0]))


