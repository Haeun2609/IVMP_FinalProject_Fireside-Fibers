import pygame
import sys
from settings import *
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

WIDTH = 1200
HEIGHT = 600
FPS = 60

pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.set_volume(0.4)

size = WIDTH / 60
firstLeft = WIDTH / 3
firstTop = 2 * HEIGHT / 3
dLeft = 17
dTop = 17
qStitches = []
stitch_images = []

rStitch_images = ['rStitch_red.png', 'rStitch_cream.png']
lStitch_images = ['lStitch_red.png', 'lStitch_cream.png']

needle_img = "needle1.png"
needle_center_x = firstLeft + 17/2
needle_center_y = firstTop + 17/2

bg_img = pygame.image.load("bg.png")
bg_rect = bg_img.get_rect()
tittle_img = pygame.image.load("tittle.png")
tittle_rect = tittle_img.get_rect(center = (WIDTH/2,HEIGHT/3))
zen_img = pygame.image.load("zen.png")
zen_rect = zen_img.get_rect(center = (WIDTH/2, HEIGHT-200))
colorwork_img = pygame.image.load("colorwork.png")
colorwork_rect = colorwork_img.get_rect(center = ((WIDTH/2, HEIGHT-140)))
timeattack_img = pygame.image.load("timeattack.png")
timeattack_rect = timeattack_img.get_rect(center = (WIDTH/2, HEIGHT-70))
pattern_img = pygame.image.load("pattern.png")
pattern_rect = pattern_img.get_rect(topright = (WIDTH - 20, 20))

keySequence = [pygame.K_q, pygame.K_SPACE, pygame.K_p, pygame.K_SPACE]
currentIndex = 0

timer = pygame.time.get_ticks()
last_correct = pygame.time.get_ticks()
wrongCount = 0

# Game states
START_SCREEN = 0
ZEN_MODE = 1
COLORWORK_MODE = 2
TIME_ATTACK_MODE = 3
GAME_OVER = 4

current_mode = START_SCREEN
font_name = pygame.font.match_font('arial')

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fireside Fibers by hbn")
clock = pygame.time.Clock()

def draw_text(surf, text, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surf.blit(text_surface, text_rect)

def time_format(milliseconds):
    seconds = milliseconds // 1000
    return f"{30 - seconds:02d}"

pygame.mixer.music.play(loops=-1)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if current_mode == START_SCREEN:
                if event.key == pygame.K_1:
                    current_mode = ZEN_MODE
                    qStitches = []
                    stitch_images = []
                    needle_img = "needle1.png"
                    needle_center_x = firstLeft + 17/2
                    needle_center_y = firstTop + 17/2
                    currentIndex = 0
                    wrongCount = 0
                elif event.key == pygame.K_2:
                    current_mode = COLORWORK_MODE
                    qStitches = []
                    stitch_images = []
                    needle_img = "needle1.png"
                    needle_center_x = firstLeft + 17/2
                    needle_center_y = firstTop + 17/2
                    currentIndex = 0
                    currentColor = 0
                    colorStitch = []
                elif event.key == pygame.K_3:
                    current_mode = TIME_ATTACK_MODE
                    qStitches = []
                    stitch_images = []
                    needle_img = "needle1.png"
                    needle_center_x = firstLeft + 17/2
                    needle_center_y = firstTop + 17/2
                    currentIndex = 0
                    time_attack_timer = pygame.time.get_ticks()
            else:
                if event.key == pygame.K_r:
                    current_mode = START_SCREEN

            #Event handling for colorwork mode
            if current_mode == COLORWORK_MODE:
                if currentIndex == 0:
                    if pygame.K_1 <= event.key <= pygame.K_2:
                        currentColor = event.key - pygame.K_1
                        if not qStitches:
                            qStitches.append(pygame.Rect((firstLeft, firstTop, size, size)))
                            colorStitch.append(lStitch_images)
                            stitch_images.append(colorStitch[-1][currentColor])
                        elif (qStitches[-1].left + dLeft >= 2 * WIDTH / 3) or (qStitches[-1].left + dLeft < WIDTH / 3):
                            dLeft *= -1
                            newQ = pygame.Rect((qStitches[-1].left, qStitches[-1].top - dTop, size, size))
                            qStitches.append(newQ)
                            for stitch in qStitches:
                                stitch.top += dTop
                            colorStitch.append(lStitch_images if colorStitch[-1] == lStitch_images else rStitch_images) 
                            stitch_images.append(colorStitch[-1][currentColor])
                        else:
                            newQ = pygame.Rect((qStitches[-1].left + dLeft, qStitches[-1].top, size, size))
                            qStitches.append(newQ)
                            # Update stitch image list
                            colorStitch.append(lStitch_images if colorStitch[-1] == rStitch_images else rStitch_images) 
                            stitch_images.append(colorStitch[-1][currentColor])
                        needle_center_x, needle_center_y = qStitches[-1].center
                        needle_img = "needle2.png" if needle_img == "needle1.png" else "needle1.png"
                        currentIndex = (currentIndex + 1) % len(keySequence)
                elif event.key == keySequence[currentIndex]:
                    if event.key == pygame.K_p:
                        if (qStitches[-1].left + dLeft >= 2 * WIDTH / 3) or (qStitches[-1].left + dLeft < WIDTH / 3):
                            dLeft *= -1
                            newQ = pygame.Rect((qStitches[-1].left, qStitches[-1].top - dTop, size, size))
                            qStitches.append(newQ)
                            for stitch in qStitches:
                                stitch.top += dTop
                            colorStitch.append(lStitch_images if colorStitch[-1] == lStitch_images else rStitch_images) 
                            stitch_images.append(colorStitch[-1][currentColor])
                        else:
                            newQ = pygame.Rect((qStitches[-1].left + dLeft, qStitches[-1].top, size, size))
                            qStitches.append(newQ)
                            # Update stitch image list
                            colorStitch.append(lStitch_images if colorStitch[-1] == rStitch_images else rStitch_images) 
                            stitch_images.append(colorStitch[-1][currentColor])
                        needle_center_x, needle_center_y = qStitches[-1].center
                        needle_img = "needle2.png" if needle_img == "needle1.png" else "needle1.png"
                    elif event.key == pygame.K_SPACE:
                        needle_center_x, needle_center_y = qStitches[-1].center
                        needle_img = "needle2.png" if needle_img == "needle1.png" else "needle1.png"
                    currentIndex = (currentIndex + 1) % len(keySequence)

            #event handling for zen and time attact mode
            if current_mode == ZEN_MODE or current_mode == TIME_ATTACK_MODE:
                if event.key == keySequence[currentIndex]:
                    if event.key == pygame.K_q or event.key == pygame.K_p:
                        if not qStitches:
                            qStitches.append(pygame.Rect((firstLeft, firstTop, size, size)))
                            stitch_images.append("lStitch.png")
                        elif (qStitches[-1].left + dLeft >= 2 * WIDTH / 3) or (qStitches[-1].left + dLeft < WIDTH / 3):
                            dLeft *= -1
                            newQ = pygame.Rect((qStitches[-1].left, qStitches[-1].top - dTop, size, size))
                            qStitches.append(newQ)
                            for stitch in qStitches:
                                stitch.top += dTop
                            stitch_images.append("lStitch.png" if stitch_images[-1] == "lStitch.png" else "rStitch.png")
                        else:
                            newQ = pygame.Rect((qStitches[-1].left + dLeft, qStitches[-1].top, size, size))
                            qStitches.append(newQ)
                            # Update stitch image list
                            stitch_images.append("lStitch.png" if stitch_images[-1] == "rStitch.png" else "rStitch.png")
                        needle_center_x, needle_center_y = qStitches[-1].center
                        needle_img = "needle2.png" if needle_img == "needle1.png" else "needle1.png"
                    elif event.key == pygame.K_SPACE:
                        needle_center_x, needle_center_y = qStitches[-1].center
                        needle_img = "needle2.png" if needle_img == "needle1.png" else "needle1.png"

                    last_correct = pygame.time.get_ticks()
                    currentIndex = (currentIndex + 1) % len(keySequence)
                    wrongCount = 0

                else:
                    wrongCount += 1

    screen.fill(BLACK)
    screen.blit(bg_img,bg_rect)
    if current_mode == START_SCREEN:
        screen.blit(tittle_img,tittle_rect)
        screen.blit(zen_img,zen_rect)
        screen.blit(colorwork_img,colorwork_rect)
        screen.blit(timeattack_img,timeattack_rect)
    
    elif current_mode == GAME_OVER:
        screen.fill(BLACK)
        screen.blit(bg_img,bg_rect)
        total_stitches = len(qStitches)
        draw_text(screen, "Game Over", 64, WIDTH / 2, HEIGHT / 4, WHITE)
        draw_text(screen, f"Total Stitches: {total_stitches}", 36, WIDTH / 2, HEIGHT / 2, WHITE)
        draw_text(screen, "Press 'R' to Restart", 36, WIDTH / 2, HEIGHT / 1.7, WHITE)

    else:
        if current_mode == TIME_ATTACK_MODE:
            elapsedTime = pygame.time.get_ticks() - time_attack_timer
            if elapsedTime > 30000:
                current_mode = GAME_OVER
            else:
                remaining_time = 30000 - elapsedTime
                timer_text = time_format(remaining_time)
                draw_text(screen, timer_text, 36, WIDTH // 2, 50, WHITE)
        elif current_mode == ZEN_MODE:
            elapsedTime = pygame.time.get_ticks() - last_correct
            if elapsedTime > 30000 or wrongCount > 5:
                next_key_text = chr(keySequence[currentIndex])
                draw_text(screen, next_key_text, 36, WIDTH // 2, 50, RED)
        elif current_mode == COLORWORK_MODE:
            screen.blit(pattern_img, pattern_rect)

        # Draw stitches
        for i, rect in enumerate(qStitches):
            stitch_img = pygame.image.load(stitch_images[i]).convert_alpha()
            screen.blit(stitch_img, rect.topleft)

        # Draw needle at the center of the current stitch
        needle_img_surface = pygame.image.load(needle_img).convert_alpha()
        needle_rect = needle_img_surface.get_rect(center=(needle_center_x, needle_center_y))
        screen.blit(needle_img_surface, needle_rect.topleft)
  
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
        
