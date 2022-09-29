import pygame
import random

FPS=60
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
WIDTH=500
HEIGHT=500
#初始化
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill((GREEN))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        #self.rect.x = 400
        #self.rect.y = 400
        self.speedx = 8
        
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_a]:
            self.rect.x -= self.speedx
        if self.rect.right >WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill((RED))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedx = random.randrange(-3,3)
        self.speedy = random.randrange(2,10)
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(0,WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedx = random.randrange(-3,3)
            self.speedy = random.randrange(2,10)

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    r=Rock()
    all_sprites.add(r)

running = True

#game
while running:
    clock.tick(FPS)
    #input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #更新
    all_sprites.update()
    
    #screen
    screen.fill((WHITE))
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()