# Faça um programa em Python que abra e reproduza o áudio
# de arquivo Mp3.

import pygame
pygame.init()
pygame.mixer.music.load('./audio/ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()