import pygame
from config import *

# Iincia o PYGAME
pygame.init()

# Cria a tela
pygame.display.set_caption('Primeiro Jogo Pygame') #"Título" da janela que irá ser aberta
run = True


def movement():
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1, 0)
    elif key[pygame.K_d]:
        player.move_ip(1, 0)
    elif key[pygame.K_w]:
        player.move_ip(0, -1)
    elif key[pygame.K_s]:
        player.move_ip(0, 1)

while run:
    screen.fill(BLACK)

    player.draw()    
    movement()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()