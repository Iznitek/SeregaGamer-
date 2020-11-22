import pygame
import random
import pygame as pg

cursor = pg.image.load("images\pokemon_ball.png")
pokemon = pg.image.load("images\jigglypuff.png")
run = True
window = pygame.display.set_mode((1700,900))
black = (0, 0, 0)
white = (123, 104, 238)
x = 250
y = 250
itr = 0
hit = 0
lost = 0
pygame.font.init()
myfont = pygame.font.SysFont('White', 50)

def cursor_draw(window,picture):
    position = pygame.mouse.get_pos()
    x = position[0]
    y = position[1]
    pygame.mouse.set_visible(False)
    window.blit(picture, (x - 40, y - 40))

pygame.init()

while run:
    itr += 1
    if itr == 1000:
        diox = random.randint(0, 1580)
        dioy = random.randint(0, 750)
        itr = 0
        lost += 1
    window.fill(black)

    massage = "Pokeball: " + str(hit) + "           Bot1: " + str(lost) + "           Beta 1.3  "
    text = myfont.render(massage, True, white)
    window.blit(text, (10, 850))

    window.blit(pokemon, (x, y))
    cursor_draw(window,cursor)
    pg.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            xPos = pos[0]
            yPos = pos[1]
            if (xPos > x) and (xPos < x + 150) and (yPos > y) and (yPos < y + 148):
                x = random.randint(0, 1580)
                y = random.randint(0, 750)
                itr = 0
                hit += 1

pygame.quit()
