import pygame
from Perso import perso
from pygame.locals import *

xaya = 0
screensize = (897, 672)
pygame.init()
fenetre = pygame.display.set_mode(screensize, RESIZABLE)
initjump = 0
continuer = True
RUN, PAUSE = 0, 1
etat = RUN
jump = 0
walk = 0

fond = pygame.image.load("map.png").convert_alpha()
fond = pygame.transform.scale(fond, (10176,672))


pygame.key.set_repeat(100, 25)
mario = perso("MarioSmall.gif", 96, 528)


def resize(a,x,y):
    self =  pygame.transform.scale(a, (x,y))
    return self

MarioState = 0


while continuer:


    for event in pygame.event.get():


        if event.type == QUIT:
            continuer = False
            quit()
        if event.type == KEYDOWN :
            if event.key == K_UP and jump == 0:
                jump = 1
            if event.key == K_DOWN and MarioState == 1:
                mario = perso("mariocrouch.gif", mario.x, mario.y)
            if event.key == K_LEFT:
                mario.x += -10
            if event.key == K_RIGHT:
                mario.x += 10
            if event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT:
                mario = perso("MarioSmall.gif", mario.x, mario.y)
        if event.type == KEYUP :
            if event.key == K_DOWN :
                mario = perso("SuperMarioWalk3.gif", mario.x, mario.y)

    if jump == 1 and xaya<9 :
        if initjump == 0 :
            xaya = -10
            initjump = 1
        elif xaya>0:
            xaya += 1
            mario.y -= round(-2/3*(xaya**2), 0)

        else :
            xaya += 1
            mario.y += round(-2/3*(xaya**2), 0)
    else :
        initjump = 0
        jump = 0

    if MarioState == 0:
        mario.image = resize(mario.image, 42, 48)
    elif MarioState == 1 or MarioState == 2:
        mario.image = resize(mario.image, 48, 80)

    fenetre.blit(fond, (0, 0))
    fenetre.blit(mario.image, (mario.x,mario.y))
    pygame.display.update()
    pygame.time.Clock().tick(60)