"""
Crie um programa que faça ocomputador jogar jokenpo com você.
jokenpo = jogo do pedra, papel e tesoura
"""
import random
print('Jogo jokenpo!')
print('Faça a sua escolha!')
print('Digite 1 para escolher PEDRA')
print('Digite 2 para escolher PAPEL')
print('Digite 3 para escolher TESOURA')
opcaoUsuario = int(input('Digite a sua opção: '))

"""
1 - PEDRA
2 - PAPEL
3 - TESOURA
"""
# Opção escolhida pelo computador
OpcaoComputador = random.randint(1, 4)

if opcaoUsuario == 1 and OpcaoComputador == 1:
    print('Jogo EMPATADO. Ambos escolheram PEDRA')
elif opcaoUsuario == 1 and OpcaoComputador == 2:
    print('VENCEDOR: COMPUTADOR!!')
    print('OPCAO COMPUTADOR: PAPEL')
    print('OPCAO USUARIO: PEDRA')
elif opcaoUsuario == 1 and OpcaoComputador == 3:
    print('VENCEDOR: USUARIO!!')
    print('OPCAO COMPUTADOR: TESOURA')
    print('OPCAO USUARIO: PEDRA')
elif opcaoUsuario == 2 and OpcaoComputador == 2:
    print('Jogo EMPATADO. Ambos escolheram PAPEL')
elif opcaoUsuario == 2 and OpcaoComputador == 1:
    print('VENCEDOR: USUARIO!!')
    print('OPCAO COMPUTADOR: PEDRA')
    print('OPCAO USUARIO: PAPEL')
elif opcaoUsuario == 2 and OpcaoComputador == 3:
    print('VENCEDOR: COMPUTADOR!!')
    print('OPCAO COMPUTADOR: TESOURA')
    print('OPCAO USUARIO: PAPEL')
elif opcaoUsuario == 3 and OpcaoComputador == 3:
    print('Jogo EMPATADO. Ambos escolheram TESOURA')
elif opcaoUsuario == 3 and OpcaoComputador == 1:
    print('VENCEDOR: COMPUTADOR!!')
    print('OPCAO COMPUTADOR: PEDRA')
    print('OPCAO USUARIO: TESOURA')
elif opcaoUsuario == 3 and OpcaoComputador == 2:
    print('VENCEDOR: USUARIO!!')
    print('OPCAO COMPUTADOR: PAPEL')
    print('OPCAO USUARIO: TESOURA')




