"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
ele, lendo o nomes deles e escrevendo o nome do escolhido
"""
import random
alunoUm = input('Digite o nome do primeiro aluno: ')
alunoDois = input('Digite o nome do segundo aluno: ')
alunoTres = input('Digite o nome do terceiro aluno: ')
alunoQuatro = input('Digite o nome do quarto aluno: ')

listaDeAlunos = [alunoUm,alunoDois, alunoTres, alunoQuatro]

# Selecionando o nome escolhido
alunoEscolhido = random.sample(listaDeAlunos, 1)

print('O aluno escolhido foi: {}'.format(alunoEscolhido))