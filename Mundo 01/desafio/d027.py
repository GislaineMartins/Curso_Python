"""
Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o último nome separadamente
Exemplo: Ana Maria de Souza
primeiro = Ana
ultimo = Souza
"""

nome = input("Digite seu nome completo: ")
quebra_string = nome.split()
print('Primeiro nome: ', quebra_string[0])
ultima_posicao = len(quebra_string)
print('Ultimo nome: ', quebra_string[ultima_posicao - 1])
