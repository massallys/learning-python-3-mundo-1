#tocando mp3

import pygame

pygame.init()

pygame.mixer.music.load('replayex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

