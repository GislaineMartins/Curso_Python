"""
Faça um programa em python que abra e reproduza o audio de um arquivo MP3
"""

import pygame

# Inicializar o mixer do pygame
pygame.mixer.init()

# Carregar o arquivo MP3
pygame.mixer.music.load("Danny Gokey - We All Need.mp3")

# Tocar o arquivo MP3
pygame.mixer.music.play()

# Esperar o término da música
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)