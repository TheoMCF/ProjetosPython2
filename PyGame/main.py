import pygame
from config import *

# Iincia o PYGAME
pygame.init()

# Cria a tela
pygame.display.set_caption('Primeiro Jogo Pygame') #"Título" da janela que irá ser aberta
run = True

while run:
    clock.tick(FPS)
    screen.fill(WHITE)
    pygame.draw.line(screen, BLUE, (0,300), (WIDTH, 300))
    player.update()

    player.draw()
    enemy.draw()   

    arrow_group.update()
    arrow_group.draw(screen)
    magic_bomb_group.update()
    magic_bomb_group.draw(screen)

    if player.alive:
        if moving_left or moving_right:
            player.update_action(1) # Run
        else:
            player.update_action(0) # Idle
        if shoot:
            player.shoot()
        
        player.move(moving_left, moving_right)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True    
            if event.key == pygame.K_f:
                shoot = True
                magic_beam_bool = True
            if event.key == pygame.K_g:
                shoot = True
                magic_bomb_bool = True
            if event.key == pygame.K_w and player.alive:
                player.jump = True
            if event.type == pygame.K_ESCAPE:
                run = False
           
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
                Idle = True
            if event.key == pygame.K_d:
                moving_right = False
            # if event.key == pygame.K_f:
            #     shoot = False
            #     magic_beam_bool = False
            # if event.key == pygame.K_g:
            #     shoot = False
            #     magic_bomb_bool = False

    pygame.display.update()

pygame.quit()