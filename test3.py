#import sqlite3
#
#conn = sqlite3.connect('test_db.sqlite')
#cursor = conn.cursor()
#code = 1
#
#cursor.execute('''SELECT * FROM users WHERE id = ?''', (code,))
#res = cursor.fetchone()
#print(res)
#conn.commit()
#
#conn.close()

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((2200, 1170))
name = pygame.display.set_caption("The nightmare")
bg = pygame.image.load("room-1.jpg")
x = 0
y = 0
active = True
left = True
right = True
check = False
open_d = False
flashlight = 0
stop = 15
secret = 0
sec_act = False
sec_act2 = False
m_act = True
m_stop = 0
monster = False
m_wait = 0
room = True
door = False

screen.blit(bg, (x, y))

while active:
    pygame.time.delay(1)
    if m_act:
        m_stop = random.randint(1000, 1500)
        m_act = False
    if m_stop != 0:
        m_stop -= 1
    if stop != 0:
        stop -= 1
    if m_stop == 0:
        monster = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    if m_wait > 1500 and room:
        bg = pygame.image.load("room-8.jpg")
        door = False
    elif m_wait > 900 and room:
        bg = pygame.image.load("room-10.jpg")
    if m_wait > 900 and door:
        bg = pygame.image.load("room-11.jpg")

    key = pygame.key.get_pressed()
    if key[pygame.K_a] and x != 0 and left:
        x += 8
    if key[pygame.K_d] and x != -600 and right:
        x -= 8
    if x == 0:
        if key[pygame.K_w] and not m_wait > 1500:
            bg = pygame.image.load("room-2.jpg")
            if m_wait > 900 and door:
                bg = pygame.image.load("room-11.jpg")
            if m_wait > 1500 and door:
                active = False
            room = False
            door = True
            right = False
            left = False
            check = True
        if key[pygame.K_s]:
            bg = pygame.image.load("room-1.jpg")
            room = True
            door = False
            right = True
            left = True
            check = False
        if key[pygame.K_e] and check:
            bg = pygame.image.load("room-3.jpg")
            open_d = True
            if m_wait > 900 and door:
                active = False
        if key[pygame.K_q] and check:
            bg = pygame.image.load("room-2.jpg")
            open_d = False
            if monster:
                monster = False
                m_act = True
        if key[pygame.K_SPACE] and check and open_d and stop == 0:
            if flashlight == 0:
                flashlight = 1
            else:
                flashlight = 0
            if flashlight == 0:
                bg = pygame.image.load("room-3.jpg")
            else:
                if m_wait >= 300:
                    bg = pygame.image.load("room-6.jpg")
                elif m_wait >= 10:
                    bg = pygame.image.load("room-5.jpg")
                else:
                    bg = pygame.image.load("room-4.jpg")
            stop = 15
    if key[pygame.K_6] and not check:
        sec_act = True
    if key[pygame.K_UP] and not check:
        sec_act2 = True
    if sec_act and sec_act2:
        monster = False
        secret += 1
        m_stop = random.randint(2000, 2200)
        if secret == 200:
            bg = pygame.image.load("room-secret.jpg")
        if secret == 450:
            bg = pygame.image.load("room-secret-2.jpg")
        if secret == 600:
            bg = pygame.image.load("room-secret-3.jpg")
        if secret == 1001:
            x = 0
            left = False
            right = False
            bg = pygame.image.load("room-secret-4.jpg")
        if secret == 1002:
            bg = pygame.image.load("room-secret-5.jpg")
        if secret == 1003:
            bg = pygame.image.load("room-secret-4.jpg")
        if secret == 1004:
            screen.fill((0, 0, 0))
        if secret == 1005:
            active = False
    if monster:
        m_wait += 1
    if not monster:
        m_wait = 0
    if m_wait > 1600:
        active = False
    screen.blit(bg, (x, y))
    pygame.display.update()
