import pygame
from Perso import perso
from platforms import Platform
from pygame.locals import *


blocks = [(20,8),(22,8),(24,8),(78,8),(80,8),(81,4),(82,4),(83,4),(85,4),(86,4),(87,4),(88,4),(91,4),(92,4),(93,4),(94,8),(100,8),(101,8),(118,8),(123,4),(121,4),(122,4),(128,4),(129,8),(130,8),(130,4),(168,8),(169,8),(171,8),(198,11)]
luckbl = [(16,8,10),(22,4,10),(21,8,11),(23,8,10),(79,8,11),(94,4,10),(106,8,10),(109,8,10),(109,4,12),(112,8,10),(129,4,10),(130,4,10),(170,4,10)]
hardbl = [(134,11),(135,10),(135,11),(136,10),(136,11),(136,9),(137,8),(137,9),(137,10),(137,11),(140,8),(140,9),(140,10),(140,11),(141,9),(141,10),(141,11),(142,10),(142,11),(143,11),(148,11),(149,10),(149,11),(150,9),(150,10),(150,11),(151,8),(151,9),(151,10),(151,11),(152,8),(152,9),(152,10),(152,11),(155,8),(155,9),(155,10),(155,11),(156,9),(156,10),(156,11),(157,10),(157,11),(158,11),(188,4),(189,4),(190,4),(187,5),(188,5),(189,5),(190,5),(186,6),(187,6),(188,6),(189,6),(190,6),(185,7),(186,7),(187,7),(188,7),(189,7),(190,7),(184,8),(185,8),(186,8),(187,8),(188,8),(189,8),(190,8),(183,9),(184,9),(185,9),(186,9),(187,9),(188,9),(189,9),(190,9),(182,10),(183,10),(184,10),(185,10),(186,10),(187,10),(188,10),(189,10),(190,10),(181,11),(182,11),(183,11),(184,11),(185,11),(186,11),(187,11),(188,11),(189,11),(190,11)]
piphg = [(29,10,2),(39,9,3),(47,8,4),(58,8,4),(163,10,2),(179,10,2)]
globgr = [(0,12),(15,12),(30,12),(45,12),(54,12),(71,12),(89,12),(89,12),(104,12),(119,12),(134,12),(138,12),(155,12),(170,12),(185,12),(200,12),(215,12)]
goombapos = [(21,11),(41,11),(49,11),(50,11),(78,7),(81,3),(99,11),(100,11),(101,11),(102,11),(126,11),(127,11),(177,11),(178,11)]
pygame.init()
start = 0
arret = 0
xmomentum,ymomentum = 0,0
points = 0
white = Color(255,255,255)
coordlist=[]
screensize = (897, 672)
fenetre = pygame.display.set_mode(screensize, RESIZABLE)
continuer = True
RUN, PAUSE = 0, 1
etat = RUN
jump_sound = pygame.mixer.Sound("jump.wav")
main_theme = pygame.mixer.music.load("smbros.wav")
pygame.mixer.music.play(-1)
jump = 0
walk = 0
initjump = 0
coins = 0
X=0
MarioState = 0
walk = 0
orientation = "D"
liste1,liste2,liste3,liste4 = [],[],[],[]

niveau = [
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,0,0,3,3,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,3,2,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,3,2,3,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,3,0,0,0,0,0,2,0,0,2,0,0,2,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,3,3,2,3,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
   ]



fond = pygame.image.load("map.png").convert_alpha()
fond = pygame.transform.scale(fond, (10176, 672))
splash = pygame.image.load("Smb splash.png").convert_alpha()
splash = pygame.transform.scale(splash, (897,672))

blocplein = Platform(960, 384, 48, 48, "BlocPlein.gif")
brique = Platform(960, 384, 48, 48, "brique.gif")
globalgr = Platform(960, 384, 720, 96, "global_ground.png")
luckblo = Platform(960,384, 48,48, "QuestionBlock.gif")
pipe = Platform(960,384, 96,192, "tuyauseul.png")
goomba = Platform(960,384, 48,48, "Goomba.gif")


pygame.key.set_repeat(100, 25)
mario = perso("MarioSmall.gif", 96, 528, 42, 48)


def resize(a,x,y):
    self = pygame.transform.scale(a, (x,y))
    return self


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def message_display(text,a,b):
    largeText = pygame.font.Font('SuperMario256.ttf',25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (a,b)
    fenetre.blit(TextSurf, TextRect)

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
            quit()

        if event.type == KEYDOWN :
            if event.key == K_SPACE :
                start = 1
            if event.key == K_LEFT:
                xmomentum = -0.5
                orientation = "G"
                if walk < 1:
                    mario = perso("MarioSmallWalk1.gif", mario.x, mario.y, 42,48)
                    mario.image = pygame.transform.flip(mario.image, True, False)
                    walk += 0.5
                elif 1 <= walk < 2:
                    mario = perso("MarioSmallWalk2.gif", mario.x, mario.y, 42, 48)
                    mario.image = pygame.transform.flip(mario.image, True, False)
                    walk += 0.5
                elif walk >= 2:
                    mario = perso("MarioSmallWalk3.gif", mario.x, mario.y, 42,48)
                    mario.image = pygame.transform.flip(mario.image, True, False)
                    walk = 0
            if event.key == K_RIGHT:
                xmomentum = 0.5
                orientation = "D"
                if walk < 1:
                    mario = perso("MarioSmallWalk1.gif", mario.x, mario.y,42,48)
                    walk += 0.5
                elif 1 <= walk < 2:
                    mario = perso("MarioSmallWalk2.gif", mario.x, mario.y,42,48)
                    walk += 0.5
                elif walk >= 2:
                    mario = perso("MarioSmallWalk3.gif", mario.x, mario.y,42,48)
                    walk = 0
            if event.key == K_UP and jump == 0:
                pygame.mixer.Sound.play(jump_sound)
                mario = perso("MarioJump.gif", mario.x, mario.y,42,48)
                ymomentum = -10

            if event.key == K_DOWN and MarioState == 1:
                mario = perso("mariocrouch.gif", mario.x, mario.y,42,48)

        if event.type == KEYUP :
            if event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT or event.key == K_UP:
                mario = perso("MarioSmall.gif", mario.x, mario.y,42,48)


        if event.type == KEYDOWN :
            print(niveau[int(mario.y // 48)][int((mario.x - X) // 48 + 1)])
            if event.key == K_RIGHT and xmomentum<7:
                if niveau[int(mario.y//48)][int((mario.x-X)//48+1)]==0:
                    xmomentum += 8
                elif niveau[int(mario.y//48)][int((mario.x-X)//48+1)]==1:
                    xmomentum = 0
                    arret = 1
                elif niveau[int(mario.y // 48+1)][int((mario.x - X ) // 48 )]>1 :
                    xmomentum = 1
                    ymomentum = -ymomentum


            if event.key == K_LEFT and xmomentum>-7 :
                if niveau[int(mario.y // 48)][int((mario.x - X) // 48 - 1)] == 0:
                    xmomentum -= 8
                elif niveau[int(mario.y // 48)][int((mario.x - X) // 48 - 1)] == 1 :
                    xmomentum = 0
                    arret = 1

            if event.key== K_UP and ymomentum>7 :
                if niveau[int(mario.y // 48+1)][int((mario.x ) // 48)] == 0:
                    ymomentum = -ymomentum
                elif niveau[int(mario.y // 48+1)][int((mario.x ) // 48 )] == 1 :
                    xmomentum = 0
                    ymomentum = 0
                    arret = 1
                else:
                    ymomentum += 5


        elif arret == 1:
            xmomentum = xmomentum / 15


    mario.x += xmomentum
    if ymomentum != 0 and 0 <= jump <= 197:
        mario.y += ymomentum
        jump -= ymomentum
    elif jump >= 197:
        jump = 197
        ymomentum = -ymomentum
    elif jump < 0:
        jump = 0
        ymomentum = 0
    xmomentum = xmomentum - .15 if xmomentum > 0 else xmomentum + .15


    if mario.x >= 448 :
        X -= xmomentum
        mario.x -= xmomentum


    if MarioState == 0:
        mario.image = resize(mario.image, 42, 48)
    elif MarioState == 1 or MarioState == 2:
        mario.image = resize(mario.image, 48, 80)

    if start == 0 :
        fenetre.blit(splash,(0,0))
    if start == 1 :
        fenetre.blit(fond, (X, 0))

        pygame.draw.rect(fenetre, pygame.Color(92, 148, 252), pygame.Rect(0, 0, 10176, 672))
        for i in range(0, len(piphg)-1):
            fenetre.blit(pipe.image, (piphg[i][0] * 48 + X, piphg[i][1] * 48))
        for i in range(0, len(blocks)-1):
            fenetre.blit(brique.image, (round(blocks[i][0]*48 + X,0), round(blocks[i][1]*48,0)))
        for i in range(0, len(hardbl) - 1):
            fenetre.blit(blocplein.image, (round(hardbl[i][0] * 48 + X,0), round(hardbl[i][1] * 48,0)))
        for i in range(0, len(globgr) - 1):
            fenetre.blit(globalgr.image, (round(globgr[i][0] * 48 + X,0), round(globgr[i][1] * 48)))
        for i in range(0, len(luckbl) - 1):
            fenetre.blit(luckblo.image, (luckbl[i][0] * 48 + X, luckbl[i][1] * 48))
        for i in range(0, len(goombapos) - 1):
            fenetre.blit(goomba.image, (goombapos[i][0] * 48 + X, goombapos[i][1] * 48))
        fenetre.blit(mario.image, (round(mario.x,0),round(mario.y,0)))
        message_display("score : " + str(points), 70, 30)
        message_display('coins : ' + str(coins), 70, 60)
    pygame.display.update()
    pygame.time.Clock().tick(80)