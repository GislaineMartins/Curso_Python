"""
Trabalhando com módulos ou bibliotecas e como utiliza-las no projetos. Nesse exemplo importa a
biblioteca random e emoji(uma biblioteca externa que é feito por outras pessoas) como exemplo
random = gera numeros aleatorios

Esse exemplo pode ser encontrado no video 24 da playlist
"""
import emoji
import random
num = random.random()
print(num)
#A função randint() serve para escolher um numero intero dentro de um intervalo. No exemplo abaixo,
# o intervalo vai de 1 até 10
numeroDois = random.randint(1,10)
print(numeroDois)

print('Emojis')
print(emoji.emojize('Hoje comer em um restaurante novo 😛'))
print(emoji.emojize('Ola mundo: 🌍'))
