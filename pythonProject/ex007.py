"""
Trabalhando com String
- Transformação
- Divisão
-
"""
frase = 'Curso em Vídeo Python'
# Mostra a letra na posição 3
print(frase[3])
# Mostra da letra na posição 3 até a posição 13-1 = 12
print(frase[3:13])
# Mostra posição inicial até a posição 13-1 = 12
print(frase[:13])
# Mostra posição 13 até a posição final
print(frase[13:])
# Mostra posição 1 até a posição 15-1 = 14
print(frase[1:15])
# Mostra posição 1 até a posição 15-1 = 14
print(frase[1:15])
# Mostra a string inteira, pulando de 2 em 2
print(frase[::2])

# Mostra a quantidade de letras 'o' dentro da lista
print(frase.count('o'))
# Mostra o tamanho da frase
print(len(frase))
# Mostra a frase excluindo os espaços em branco antes e depois da grase
print(len(frase.strip()))
# Troca uma palavra por outra dentro da frase
print(frase.replace('Python','Android'))
# Salva a alteração feita na linha acima
frase = frase.replace('Python','Android')
print(frase)

#Encontra a posição da palavra
print(frase.find('Vídeo'))

# Dividindo a frase
dividido = frase.split()
print(dividido)

# Pegar a primeira posição depois de dividir a frase
print(dividido[0])
# Pegar a primeira posição depois mostre a letra que esta na posição 3
print(dividido[0][3])


#Outra forma de escrever uma string em forma de texto
print("""
Welcome! Are you completely ney to programming? about why and how to get started with Python. 
Fortunately an experienced programmer in any programming language (whatever it may be) can pick up
Python very quickly. Its also easy for beginners to use and learn, so jump in!""")


