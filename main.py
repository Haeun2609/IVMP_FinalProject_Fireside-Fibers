import pygame
import random
from os import path

from pygame.sprite import _Group

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH =  800
HEIGHT = 450
FPS = 60

#Define color
BLACK = (0,0,0)
WHITE = (255,255,255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fireside Fibers")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def newstitch():
    s = Stitchs()
    stitches.add(s)

class Stitchs(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(stitch_images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 4
        self.rect.centery = HEIGHT - 20
        self.dx = self.rect.width
        self.dy = self.rect.height
    
    def add(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_q]:
            self.rect.centerx += self.dx
            self.rect.centery -= self.dy
        if keystate[pygame.K_SPACE]:
            self.rect.centery += self.dy
        if keystate[pygame.K_p]:
            self.rect.centerx += self.dx
            self.rect.centery -= self.dy
        if self.rect.right > (WIDTH/4) + (self.rect.width * 10):
            self.rect.centery += self.dy

#Load all game graphics
background = pygame.image.load(path.join(img_dir, "bg.png")).convert()
background_rect = background.get_rect()
stitch_images = []
stitch_list = ['st1.png','st2.png','st3.png','st4.png']
for img in stitch_list:
    stitch_images.append(pygame.image.load(path.join(img_dir,img)).convert())

stitches = pygame.sprite.Group()

#Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render
    screen.fill(WHITE)
    screen.blit(background,background_rect)
    stitches.draw(screen)
    pygame.display.flip()

pygame.quit()
