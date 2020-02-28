import pygame
from Perso import perso
from pygame.locals import *

start = 0
tempy= 0
xaya = -10

screensize = (897, 672)
pygame.init()
fenetre = pygame.display.set_mode(screensize, RESIZABLE)
continuer = True
RUN, PAUSE = 0, 1
etat = RUN
jump_sound = pygame.mixer.Sound("jump.wav")
jump = 0
walk = 0
xaya = -11
initjump = 0


fond = pygame.image.load("map.png").convert_alpha()
fond = pygame.transform.scale(fond, (10176, 672))
splash = pygame.image.load("Smb splash.png").convert_alpha()



pygame.key.set_repeat(100, 25)
mario = perso("MarioSmall.gif", 96, 528)


def resize(a,x,y):
    self =  pygame.transform.scale(a, (x,y))
    return self


MarioState = 0
walk = 0
orientation = "D"

with open("entities.txt", "r") as entities:
    for ligne in entities:
        print(ligne[9:].split(";"))


while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
            quit()

        if event.type == KEYDOWN :
            if event.key == K_SPACE :
                start = 1
            if event.key == K_UP and jump == 0:
                jump = 1
                pygame.mixer.Sound.play(jump_sound)
                tempy = mario.y
                mario = perso("MarioJump.gif", mario.x, mario.y)
            if event.key == K_DOWN and MarioState == 1:
                mario = perso("mariocrouch.gif", mario.x, mario.y)
            if event.key == K_LEFT:
                mario.x += -10
                orientation = "G"
                if walk == 0:
                    mario = perso("MarioSmallWalk1.gif", mario.x, mario.y)
                    walk += 1
                elif walk == 1:
                    mario = perso("MarioSmallWalk2.gif", mario.x, mario.y)
                    walk += 1
                elif walk == 2:
                    mario = perso("MarioSmallWalk3.gif", mario.x, mario.y)
            if event.key == K_RIGHT:
                mario.x += 10
                orientation = "D"
                if walk == 0:
                    mario = perso("MarioSmallWalk1.gif", mario.x, mario.y)
                    walk += 1
                elif walk == 1:
                    mario = perso("MarioSmallWalk2.gif", mario.x, mario.y)
                    walk += 1
                elif walk == 2:
                    mario = perso("MarioSmallWalk3.gif", mario.x, mario.y)
                    walk = 0

        if event.type == KEYUP :
            if event.key == K_RIGHT:
                mario.x += 10
            if event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT or event.key == KEYUP:
                mario = perso("MarioSmall.gif", mario.x, mario.y)
        if jump == 1 and xaya < 10 :
            if xaya>0:
                xaya += 1
                mario.y -= round(-(xaya**2), 0)
            else :
                xaya += 1
                mario.y += round(-2/3*(xaya**2), 0)
            if xaya == 10:
                mario.y = tempy
                if MarioState == 0 :
                    mario = perso("MarioSmall.gif", mario.x, mario.y)
                if MarioState == 1 :
                    mario = perso("SuperMario.gif", mario.x, mario.y)

        else :
            jump = 0
            xaya =-11


        if MarioState == 0:
            mario.image = resize(mario.image, 42, 48)
        elif MarioState == 1 or MarioState == 2:
            mario.image = resize(mario.image, 48, 80)


        if start == 0 :
            fenetre.blit(splash,(0,0))
        if start == 1 :
            fenetre.blit(fond, (0, 0))
            fenetre.blit(mario.image, (mario.x,mario.y))
        pygame.display.update()
        pygame.time.Clock().tick(60)
