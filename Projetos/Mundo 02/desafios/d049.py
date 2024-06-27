""""
Refaça o desafio 009(tabuada), mostrando a tabuada de um número que o usuário escolher, só que
agora utilizando um laço for
"""

n = int(input('Digite um numero: '))
print('*********TABUADA*********')

for i in range(1,n):
    print('{} x {} = {}'.format(i,n, i*n))