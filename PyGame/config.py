import pygame
import os

# Imagens:
# Projéteis:


# Cores:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Dimensões da Tela:
WIDTH = 1920 / 2
HEIGHT = 1080 / 2

# Ações:
moving_left = False
moving_right = False
shoot = False
magic_beam_bool = False
magic_bomb_bool = False

# FPS:
clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Criando o player:
class Hero(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.shooting_cooldown = 0
        self.direction = 1
        self.vel_y = 0
        self.in_air = True
        self.jump = False
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        animation_types = ['Idle','Walk','Shot','Dead']
        for animation in animation_types:
            temp_list = []
            num_of_frames = len(os.listdir(f'PyGame\imgs\{self.char_type}\{animation}'))
            for i in range(1, num_of_frames):
                Hero = pygame.image.load(f'PyGame\imgs\{self.char_type}\{animation}\{"__"}{i}.png').convert_alpha()
                Hero = pygame.transform.scale(Hero, (Hero.get_width() * scale, Hero.get_height() * scale))
                temp_list.append(Hero)
            self.animation_list.append(temp_list)

        self.Hero = self.animation_list[self.action][self.frame_index]
        self.rect = self.Hero.get_rect()
        self.rect.center = (x, y)
    
    def update(self):
        self.update_animation()
        
        if self.shooting_cooldown > 0:
            self.shooting_cooldown -= 1
        
        if pygame.sprite.spritecollide(player, arrow_group, True):
            if player.alive:
                self.kill()
        
        if pygame.sprite.spritecollide(enemy, magic_bomb_group, True):
            if player.alive:
                self.kill()
    def move(self, moving_left, moving_right):
        GRAVITY = 0.75
        dx = 0
        dy = 0
    
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        # Pulo
        if self.jump == True and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True
        # Aplica gravidade
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y
        #Cria a colisão do chão 
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False

        self.rect.x += dx
        self.rect.y += dy

    def shoot(self):
        if self.shooting_cooldown == 0 and self.ammo > 0 and magic_bomb_bool:
            self.shooting_cooldown = 150
        elif self.shooting_cooldown == 0 and self.ammo > 0 and magic_beam_bool:
            self.shooting_cooldown = 150
            self.update_action(2) #Shoot
            magic_bomb = Magic_Bomb(self.rect.centerx + (self.rect.size[0] * self.direction), self.rect.centery, self.direction)
            magic_bomb_group.add(magic_bomb)
            self.ammo -= 1

    # Muda as animações
    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.Hero = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0


    # Atualiza as ações
    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.Hero, self.flip, False), self.rect)

# Enemy:
arrow = pygame.image.load('PyGame/imgs/enemy/Projectiles/arrow.png').convert_alpha()
arrow_left = pygame.image.load('PyGame/imgs/enemy/Projectiles/arrow_left.png').convert_alpha()
# Player:
magic_shot = pygame.image.load('PyGame/imgs/player/Projectiles/magic_shot.png').convert_alpha()
magic_shot_left = pygame.image.load('PyGame/imgs/player/Projectiles/magic_shot_left.png').convert_alpha()
magic_beam = pygame.image.load('PyGame\imgs\player\Projectiles\magic_shot.png').convert_alpha()
magic_beam_left = pygame.image.load('PyGame\imgs\player\Projectiles\magic_shot_left.png').convert_alpha()

class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 7
        self.image = arrow
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
        if enemy.direction == -1:
            self.image = arrow_left
        else:
            self.image = arrow
        
    def update(self):
        self.rect.x += (8 * self.direction)    
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class Magic_Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 7
        self.image = magic_shot
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
        if player.direction == -1:
            self.image = magic_shot_left
        else:
            self.image = magic_shot
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()
    def update(self):
        self.rect.x += (8 * self.direction)
arrow_group = pygame.sprite.Group()
magic_bomb_group = pygame.sprite.Group()

player = Hero('player',200, 200, 1, 6, 5)
enemy = Hero('enemy', 200, 260, 1, 6, 10000)