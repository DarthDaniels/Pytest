import pygame

pygame.init()

screen = pygame.display.set_mode((2200, 1170))
name = pygame.display.set_caption("test")
pygame.mixer.music.load("music.mp3")
bg = pygame.image.load("Open-House.png")
pygame.mixer.music.set_volume(1)
active = False


def game_t():
    global active
    #pygame.mixer.music.play(1)
    active = True


game_t()

while active:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    screen.blit(bg, (50, 50))
    pygame.display.update()
