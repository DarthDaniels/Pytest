import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1500, 1000))
screen.fill((0, 0, 0))

circle_img = pygame.image.load("Circle.png")
player1_img = pygame.image.load("Player.png")
player2_img = pygame.image.load("Player.png")

width = 64
height = 250
x_play1 = 50 + width
y_play1 = 500 - height
x_play2 = 1400 - width
y_play2 = 500 - height
x_circle = 750
y_circle = 500
x_speed = 1
y_speed = 1
up = 0
left = False
right = True
active = True
act_r = True

while act_r:
    upper = random.randint(1, 2)
    if upper == 1 and y_circle < 990:
        y_speed = 1
    else:
        y_speed = -1
    act_r = False

while active:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and y_play1 > 50:
        y_play1 -= 1
    if key[pygame.K_s] and y_play1 < 950 - height:
        y_play1 += 1
    if key[pygame.K_UP] and y_play2 > 50:
        y_play2 -= 1
    if key[pygame.K_DOWN] and y_play2 < 950 - height:
        y_play2 += 1

    if (x_circle == x_play2 and y_circle > y_play2) and y_circle < (y_play2 + height + 82):
        left = True
        right = False
    if ((x_circle == x_play1 + width) and y_circle > y_play1) and y_circle < (y_play1 + height + 82):
        left = False
        right = True

    if left:
        x_circle -= x_speed
        if y_circle == 100 or y_circle == 980 or up == 1:
            y_circle -= y_speed
            up = 1
        if y_circle == 100 or y_circle == 980:
            y_circle -= y_speed

    if right:
        x_circle += x_speed
        if y_circle == 100 or y_circle == 980 or up == 1:
            y_circle -= y_speed
            up = 1
        elif y_circle > 100 and (y_circle < 980):
            y_circle += y_speed

    screen.fill((0, 0, 0))
    screen.blit(player1_img, (x_play1, y_play1))
    screen.blit(player2_img, (x_play2, y_play2))
    screen.blit(circle_img, (x_circle - 42, y_circle - 82))

    pygame.display.update()
