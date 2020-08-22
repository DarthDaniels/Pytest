import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill((0, 0, 0))

power = pygame.image.load("Spr1.png")

x = 40
y = 40
height = 35
width = 20
speed = 5
active = True
jump = False
count = 10
red, green, blue = 255, 255, 255

while active:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and x > 10:
        x -= speed
    if key[pygame.K_RIGHT] and x < (500 - width - 15):
        x += speed
    if key[pygame.K_SPACE]:
        jump = True
    if jump:
        if count >= -10:
            y -= count
            count -= 1
        else:
            count = 10
            jump = False

    if key[pygame.K_UP] and y > 10 and jump == False:
        y -= speed
    if key[pygame.K_DOWN] and y < (500 - height - 15) and jump == False:
        y += speed

    screen.fill((0, 0, 0))
    screen.blit(power, (x, y))

    pygame.display.update()             

pygame.quit()
