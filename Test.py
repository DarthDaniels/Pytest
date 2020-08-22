import pygame


pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill((0, 0, 0))

x = 40
y = 40
height = 25
width = 25
speed = 1
active = True
red, green, blue = 255, 255, 255

while active:
    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    key = pygame.key.get_pressed()
    if key[pygame.K_b] and x < (500 - width - 15) and y < (500 - width - 15):
        height += 1
        width += 1
    if key[pygame.K_n]:
        height = 25
        width = 25
    if key[pygame.K_0]:
        screen.fill((0, 0, 0))
    if key[pygame.K_1]:
        red, green, blue = 255, 255, 255
    if key[pygame.K_2]:
        red, green, blue = 255, 0, 0
    if key[pygame.K_3]:
        red, green, blue = 0, 255, 0
    if key[pygame.K_4]:
        red, green, blue = 0, 0, 255
    if key[pygame.K_5]:
        red, green, blue = 255, 255, 0
    if key[pygame.K_6]:  
        red, green, blue = 255, 0, 255
    if key[pygame.K_7]:
        red, green, blue = 0, 255, 255
    if key[pygame.K_LEFT] and x > 10:
        pygame.draw.rect(screen, (red, green, blue), (x, y, width, height))
        x -= speed
    if key[pygame.K_RIGHT] and x < (500 - width - 15):
        pygame.draw.rect(screen, (red, green, blue), (x, y, width, height))
        x += speed
    if key[pygame.K_UP] and y > 10:
        pygame.draw.rect(screen, (red, green, blue), (x, y, width, height))
        y -= speed
    if key[pygame.K_DOWN] and y < (500 - height - 15):
        pygame.draw.rect(screen, (red, green, blue), (x, y, width, height))
        y += speed
    if key[pygame.K_SPACE]:
        red, green, blue = 0, 0, 0
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    pygame.draw.rect(screen, (red, green, blue), (x + 2, y + 2, width - 4, height - 4))
    pygame.display.update()

pygame.quit()
