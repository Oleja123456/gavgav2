import pygame

pygame.init()

win_width = 700
win_height = 500
FPS = 20
win = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

background_image = pygame.transform.scale(pygame.image.load('textures/background.png'), (700 , 500))
