import pygame

pygame.init()

screen = pygame.display.set_mode((2000, 1100))
name = pygame.display.set_caption("Tanks")

screen.fill((255, 255, 255))

tank = pygame.image.load("Tank.png")
tank_shot = pygame.image.load("Tank-shot.png")
bg = pygame.image.load("Backgrd.png")
x = 40
y = 40
y_speed = 0
x_speed = 1
height = 35
width = 20
active = True
flip_a = 0
flip_t = 1
stop = 0
shot = False
x_s = 0
y_s = 0
x_shot = 0
y_shot = 0
x_shot_s = 0
y_shot_s = 20
shot_speed = False

while active:
    pygame.time.delay(100)
    if stop > 0:
        stop -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    screen.fill((255, 255, 255))
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and stop == 0:
        flip_a += 90
        if flip_t >= 4:
            flip_t = 1
        else:
            flip_t += 1
        stop = 10
    if key[pygame.K_d] and stop == 0:
        flip_a -= 90
        if flip_t <= 1:
            flip_t = 4
        else:
            flip_t -= 1
        stop = 10

    if flip_t == 1:
        x_speed = 10
        y_speed = 0
    if flip_t == 2:
        x_speed = 0
        y_speed = -10
    if flip_t == 3:
        x_speed = -10
        y_speed = 0
    if flip_t == 4:
        x_speed = 0
        y_speed = 10

    if key[pygame.K_w]:
        x += x_speed
        y += y_speed
    if key[pygame.K_s]:
        x -= x_speed
        y -= y_speed
    if key[pygame.K_SPACE]:
        shot = True
        shot_speed = True
    if shot_speed:
        if flip_t == 1:
            x_shot_s = 20
            y_shot_s = 0
        if flip_t == 2:
            x_shot_s = 0
            y_shot_s = -20
        if flip_t == 3:
            x_shot_s = -20
            y_shot_s = 0
        if flip_t == 4:
            x_shot_s = 0
            y_shot_s = 20
        shot_speed = False

    while shot:
        pygame.time.delay(100)
        if x_shot == 1950:
            shot = False
        else:
            x_shot += x_shot_s
            y_shot += y_shot_s
    screen.blit(bg, (0, 0))
    flip = pygame.transform.rotate(tank, flip_a)
    screen.blit(flip, (x, y))
    screen.blit(tank_shot, (x_shot, y_shot))

    pygame.display.update()
