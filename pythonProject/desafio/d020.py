"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos quatro alunos e motre a ordem sorteadas
"""
import random
alunoUm = input('Digite o nome do primeiro aluno: ')
alunoDois = input('Digite o nome do segundo aluno: ')
alunoTres = input('Digite o nome do terceiro aluno: ')
alunoQuatro = input('Digite o nome do quarto aluno: ')

listaDeAlunos = [alunoUm,alunoDois, alunoTres, alunoQuatro]

# Selecionando o nome escolhido
alunoEscolhido = random.sample(listaDeAlunos, 4)

print('Os alunos escolhidos foram: {}'.format(alunoEscolhido))