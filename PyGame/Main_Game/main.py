import pygame
from config import *

# Iincia o PYGAME
pygame.init()

# Cria a tela
pygame.display.set_caption('Primeiro Jogo Pygame') #"Título" da janela que irá ser aberta

# LOOP PRINCIPAL DO JOGO
run = True
while run:

    clock.tick(FPS)
    screen.fill(GRAY)
    pygame.draw.line(screen, BLUE, (0,300), (WIDTH, 300))
    
    # Status
    draw_text(F"Health:", FONTE, WHITE, 10, 15) # Vida
    draw_text(F"Mana:", FONTE, WHITE, 13, 60) # Mana
    draw_text(F"Bombs:", FONTE, WHITE, 9, 100) # Quantidade de bombas
    x = 90
    for i in range(player.qnt_magic_bombs):
        screen.blit(magic_bomb_img, (x, 100))
        x += 40

    # Atualiza e desenha os jogadores e inimigos
    player.update()
    player.draw()
    for enemy in enemy_group:
        enemy.AI()
        enemy.update()
        enemy.draw()   

    # Desenha as barras de vida e de mana
    barra_de_vida.hp = player.health
    barra_de_vida.draw(screen)
    barra_de_mana.mana = player.mana
    barra_de_mana.draw(screen)

    # Atualiza e desenha os projeteis
    arrow_group.update()
    magic_shot_group.update()
    magic_bomb_group.update()
    explosion_group.update()
    items_group.update()

    arrow_group.draw(screen)
    magic_shot_group.draw(screen)
    magic_bomb_group.draw(screen)
    explosion_group.draw(screen)
    items_group.draw(screen)

    if player.alive:
        if shoot:
            player.shoot()
        elif shoot_magic_bomb and thrown_magic_bomb == False and player.qnt_magic_bombs > 0:
            magic_bomb = Magic_Bomb_Class(player.rect.centerx + (player.rect.size[0] * 0.5 * player.direction),\
                                player.rect.top, player.direction)
            magic_bomb_group.add(magic_bomb)
            player.qnt_magic_bombs -= 1
            thrown_magic_bomb = True
        elif player.in_air:
            player.update_action(4) # Jump

        elif moving_left or moving_right:
            player.update_action(1) # Run
        else:
            player.update_action(0) # Idle
        
        player.move(moving_left, moving_right)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.K_p:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True    
            if event.key == pygame.K_SPACE:
                if moving_right:
                    shoot = True
                    moving_right = True
                elif moving_left:
                    shoot = True
                    moving_left = True
                else:
                    shoot = True
            if event.key == pygame.K_f:
                shoot_magic_bomb = True
            if event.key == pygame.K_w and player.alive:
                player.jump = True
    
        if event.type == pygame.KEYUP:  
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_f:
                shoot_magic_bomb = False
                thrown_magic_bomb = False
    pygame.display.update()

pygame.quit()