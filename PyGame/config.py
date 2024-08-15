import pygame

#Colors:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Dimensões da Tela:
WIDTH = 1920 / 2
HEIGHT = 1080 / 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Criando o player:
class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        Hero = pygame.image.load('PyGame\imgs\Heroi.png')
        self.Hero = pygame.transform.scale(Hero, (Hero.get_width() * scale, Hero.get_height() * scale))
        self.rect = self.Hero.get_rect()
        self.rect.center = (x, y)
    def draw(self):
        screen.blit(self.Hero, self.rect)

player = Hero(200, 200, 0.3)




