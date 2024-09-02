import pygame
import os
import random as rdm
import csv

# Dimensões da Tela:
WIDTH = 1200
HEIGHT = 600

# Variáveis do jogo:
GRAVITY = 0.75
pygame.font.init()
FONTE = pygame.font.Font('PyGame/Main_Game/imgs/fonts/AncientModernTales-a7Po.ttf', 30)
ROWS = 16
COLS = 150
TILE_SIZE = HEIGHT // ROWS
TILE_TYPES = 21
level = 1

# Cores:
GRAY = (123, 123, 123)
DARK_GRAY = (84, 84, 84)
PINK = (255, 204, 204)
YELLOW = (255, 255, 0)
LIGHT_PURPLE = (153, 51, 255)
DARK_PURPLE = (102, 51, 153)	
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_RED = (255, 127, 127)
GREEN = (0, 255, 0)
LIGHT_GREEN = (157, 247, 119)
BLUE = (0, 0, 255)
LIGHT_BLUE = (106, 217, 213)

# Ações:
moving_left = False
moving_right = False
shoot = False
shoot_magic_bomb = False
thrown_magic_bomb = False

# FPS:
clock = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Enemy:
arrow_img = pygame.image.load('PyGame/Main_Game/imgs/enemy/Projectiles/arrow.png').convert_alpha()
arrow_left_img = pygame.image.load('PyGame/Main_Game/imgs/enemy/Projectiles/arrow_left.png').convert_alpha()

# Player:
magic_shot_img = pygame.image.load('PyGame/Main_Game/imgs/player/Projectiles/magic_shot.png').convert_alpha()
magic_shot_left_img = pygame.image.load('PyGame/Main_Game/imgs/player/Projectiles/magic_shot_left.png').convert_alpha()
magic_bomb_img = pygame.image.load('PyGame/Main_Game/imgs/player/Projectiles/magic_bomb.png').convert_alpha()

# items:
health_item_img = pygame.image.load('PyGame/Main_Game/imgs/items/heart.png').convert_alpha()
bomb_item_img = pygame.image.load('PyGame/Main_Game/imgs/items/Bomb.png').convert_alpha()
mana_item_img = pygame.image.load('PyGame/Main_Game/imgs/items/mana_potion.png').convert_alpha()

# Dicionário com as imagens dos items: 'Health', 'Bomb', 'Mana'
items = {
    'Health' : health_item_img,
    'Bomb' : bomb_item_img,
    'Mana' : mana_item_img
}

def draw_text(text, font, text_col, x,  y):
    font = font.render(text, True, text_col)
    screen.blit(font, (x, y))

# Criando o player:
class Hero(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, mana, health, qnt_magic_bombs):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.mana = mana
        self.start_mana = mana
        self.shooting_cooldown = 0
        self.qnt_magic_bombs = qnt_magic_bombs
        self.health = health
        self.max_health = self.health
        self.direction = 1
        self.vel_y = 0
        self.in_air = True
        self.jump = False
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # AI specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 150, 20)
        self.idling = False
        self.idling_counter = 0


        animation_types = ['Idle','Walk','Shot','Dead','Jump']
        for animation in animation_types:
            temp_list = []
            num_of_frames = len(os.listdir(f'PyGame/Main_Game/\imgs\{self.char_type}\Animations\{animation}'))
            if animation == 'Dead':
                num_of_frames += 1
            
            for i in range(1, num_of_frames):
                Hero = pygame.image.load(f'PyGame/Main_Game/\imgs\{self.char_type}\Animations\{animation}\__{i}.png').convert_alpha()
                Hero = pygame.transform.scale(Hero, (Hero.get_width() * scale, Hero.get_height() * scale))
                temp_list.append(Hero)
            self.animation_list.append(temp_list)

        self.Hero = self.animation_list[self.action][self.frame_index]
        self.rect = self.Hero.get_rect()
        self.rect.center = (x, y)
    
    def update(self):
        self.update_animation()
        self.check_alive()
        if self.shooting_cooldown > 0:
            self.shooting_cooldown -= 1
        
        if pygame.sprite.spritecollide(player, arrow_group, True):
            if player.alive:
                player.health -= 10
        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, magic_shot_group, True):
                if enemy.alive:
                    enemy.health -= 25
                    
    # Função de movimento
    def move(self, moving_left, moving_right):
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

    # Atira um projétil
    def shoot(self):
        if self.char_type == 'enemy':
            if self.shooting_cooldown == 0 and self.mana > 0:
                self.shooting_cooldown = 50
                arrow = Arrow_Class(self.rect.centerx + (self.rect.size[0] * self.direction), self.rect.centery, self.direction)
                arrow_group.add(arrow)
                self.mana -= 5
        elif self.char_type == 'player':
            if self.shooting_cooldown == 0 and self.mana > 0:
                self.shooting_cooldown = 50
                magic_shot = Magic_Shot_Class(self.rect.centerx + (self.rect.size[0] * self.direction), self.rect.centery, self.direction)
                magic_shot_group.add(magic_shot)
                self.mana -= 5
    def AI(self):
        if self.alive and player.alive:
            if self.idling == False and rdm.randint(1,200) == 5:
                self.idling = True
                self.update_action(0) #Idle
                for skeleton in enemy_group:
                    skeleton.rect.bottom = 305
                self.idling_counter = 50
            # Se o player estiver no campo de visao do esqueleto
            if self.vision.colliderect(player.rect):
                self.update_action(2)
                self.rect.bottom = 292
                self.shoot()
            else:    
                if self.idling == False:
                    if self.direction == 1:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)
                    for skeleton in enemy_group:
                        skeleton.rect.bottom = 303
                    self.move_counter += 1
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)
                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False
                        self.update_action(0) # Idle
                        for skeleton in enemy_group:
                            skeleton.rect.bottom = 305

    # Muda as animações
    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        #Atualiza a imagem dependendo do frame atual
        self.Hero = self.animation_list[self.action][self.frame_index]
        #Verifica se o tempo suficiente passou
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3: # Dead 
                self.frame_index = len(self.animation_list[self.action]) -1
            else:
                self.frame_index = 0

    # Atualiza as ações
    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    # Verifica se o jogador está morto
    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3) # Dead
            player.rect.bottom = 315
            for skeleton in enemy_group:
                skeleton.rect.bottom = 310

    def draw(self):
        screen.blit(pygame.transform.flip(self.Hero, self.flip, False), self.rect)

class Health_Bar():
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.mana = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        # calculate mana ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, LIGHT_RED, (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, LIGHT_GREEN, (self.x, self.y, self.w * ratio, self.h))

class Mana_Bar():
    def __init__(self, x, y, w, h, max_mana):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.mana = max_mana
        self.max_mana = max_mana

    def draw(self, surface):
        # calculate health ratio
        ratio = self.mana / self.max_mana
        pygame.draw.rect(surface, LIGHT_PURPLE, (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, DARK_PURPLE, (self.x, self.y, self.w * ratio, self.h))

class Items_Class(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        self.image = items[self.item_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))
    
    def update(self):
        if pygame.sprite.collide_rect(self, player):
            if self.item_type == 'Health':
                player.health += 30
                if player.health > player.max_health:
                    player.health = player.max_health
            elif self.item_type == 'Bomb':
                player.qnt_magic_bombs += 1
            elif self.item_type == 'Mana':
                player.mana += 25
                if player.mana > player.start_mana:
                    player.mana = player.start_mana
            self.kill()

class Arrow_Class(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 7
        self.image = arrow_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction

        # Colocar a bala na direção correta
        if enemy.direction == -1:
            self.image = arrow_left_img
        else:
            self.image = arrow_img
    def update(self):
        self.rect.x += (8 * self.direction)    
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class Magic_Shot_Class(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 7
        self.image = magic_shot_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction

        # Colocar a bala na direção correta
        if player.direction == -1:
            self.image = magic_shot_left_img
        else:
            self.image = magic_shot_img
    def update(self):
        self.rect.x += (8 * self.direction)
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class Magic_Bomb_Class(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 150
        self.vel_y = -11
        self.speed = 7
        self.image = magic_bomb_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction

    def update(self):
        self.vel_y += GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y

        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.speed = 0

        if self.rect.left + dx < 0 or self.rect.right + dx > WIDTH:
            self.direction *= -1
            dx = self.direction * self.speed

        self.rect.x += dx
        self.rect.y += dy

        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            explosion = Explosion_Class(self.rect.x, self.rect.y)
            explosion_group.add(explosion)
            # Criar dano da bomba
            if abs(self.rect.centerx - player.rect.centerx) < TILE_SIZE * 6 and \
                abs(self.rect.centery - player.rect.centery) < TILE_SIZE * 6:
                player.health -= 50
            for enemy in enemy_group:    
                if abs(self.rect.centerx - enemy.rect.centerx) < TILE_SIZE * 6 and \
                    abs(self.rect.centery - enemy.rect.centery) < TILE_SIZE * 6:
                    enemy.health -= 75
                
class Explosion_Class(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 7):
            expl_imgs = pygame.image.load(f'PyGame/Main_Game/\imgs\player\Animations\Explosion\__{i}.png').convert_alpha()
            self.images.append(expl_imgs)
        
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter = 0
        
    def update(self):
        EXPLOSION_SPEED = 4
        self.counter += 1
        if self.counter >= EXPLOSION_SPEED:
            self.counter = 0
            self.frame_index += 1
            if self.frame_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame_index]

# Criar grupos de sprites
enemy_group = pygame.sprite.Group()
arrow_group = pygame.sprite.Group()
magic_shot_group = pygame.sprite.Group()
magic_bomb_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
items_group = pygame.sprite.Group()

#temprario
item = Items_Class("Health", 400, 283)
items_group.add(item)
item = Items_Class("Bomb", 500, 287)
items_group.add(item)
item = Items_Class("Mana", 600, 297)
items_group.add(item)

# Cria o jogador, o inimigo e as barras de mana e de vida
# Valores respectivamente: Tipo do personagem, posição x e y de spawn, tamanho, velocidade, quantidade de mana, quantidade de vida, quantidade de bombas,
player = Hero('player',600, 200, 0.8, 6, 50, 100, 3)
enemy = Hero('enemy', 200, 260, 0.95, 2, 10000, 100, 0)
enemy2 = Hero('enemy', 400, 260, 0.95, 2, 10000, 100, 0)
barra_de_vida = Health_Bar(90, 10, 300, 40, player.max_health)
barra_de_mana = Mana_Bar(90, 73, 300, 10, player.start_mana)
enemy_group.add((enemy, enemy2))