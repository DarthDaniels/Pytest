import pygame

pygame.init()

screen = pygame.display.set_mode((2200, 1170))
name = pygame.display.set_caption("Test")
bg = pygame.image.load("bg.jpg")
person = pygame.image.load("Test_cord_1.png")
list_cord = [([1220, 350]), ([1220, 650]), ([1525, 350]), ([1525, 650])]  # левый верх, левый низ, правый верх, правый низ
person_width = 200
person_height = 300
active = True
x, y = 0, 0                                     # левый верх
x2, y2 = 0, 0 + person_height                   # левый низ
x3, y3 = 0 + person_width, 0                    # правый верх
x4, y4 = 0 + person_width, 0 + person_height    # правый низ

while active:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        None

    screen.blit(bg, (0, 0))
    screen.blit(person, (x, y))
    pygame.display.update()
