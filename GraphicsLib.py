import pygame

WHITE = (255, 255, 255)
ORANGE = (255, 153, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
orange=(255,153,0)
black = (0,0,0)
red = (255,25,25)

character1 = pygame.image.load('swatshootingcycle1.png')
character1= pygame.transform.scale(character1,(70,75))
character1.set_colorkey(WHITE)
character2 = pygame.image.load('swatswalkingcycle2.png')
character2= pygame.transform.scale(character2,(70,75))
character2.set_colorkey(WHITE)
#background = pygame.image.load('action cycle 3.jpg')
#background= pygame.transform.scale(background,(50,55))
Realbackground = pygame.image.load('Mbackground.png')
Realbackground= pygame.transform.scale(Realbackground,(1300,800))
characterAnimationL = [character1,character2]


enemy1 = pygame.Surface((50,50))
pygame.draw.circle(enemy1,orange,(25,25),5)
        