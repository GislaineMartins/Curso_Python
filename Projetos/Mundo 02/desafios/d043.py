"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
seu IMC e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: abaixo do peso
- Entre 18.5 e 25: peso ideal
- 25 até 30: Sobrepeso
- 30 a´te 40: Obesidade
- Acima de 40: Obesidade mórbida
"""
peso = float(input('Digite seu peso: '))
altura = float(input('Digite seu altura: '))
imc = peso/(altura * altura)

if imc < 18.5:
    print('IMC: {}! Abaixo do peso'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('IMC: {}! Peso ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('IMC: {}! Sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('IMC: {}! Obesidade'.format(imc))
else:
    print('IMC: {}! Obesidade mórbida'.format(imc))

