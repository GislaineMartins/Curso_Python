"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
ele, lendo o nomes deles e escrevendo o nome do escolhido
"""

"""
Outra forma de fazer o exercicio 19
"""
import random
alunoUm = input('Digite o nome do primeiro aluno: ')
alunoDois = input('Digite o nome do segundo aluno: ')
alunoTres = input('Digite o nome do terceiro aluno: ')
alunoQuatro = input('Digite o nome do quarto aluno: ')

listaDeAlunos = [alunoUm,alunoDois, alunoTres, alunoQuatro]

# Método choice serve para escolher alguem da lista
alunoEscolhido = random.choice(listaDeAlunos)

print('O aluno escolhido foi: {}'.format(alunoEscolhido))