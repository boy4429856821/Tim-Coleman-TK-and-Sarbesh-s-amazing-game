import pygame

WHITE = (255, 255, 255)
ORANGE = (255, 153, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


character1 = pygame.image.load('swatshootingcycle1.png')
character1= pygame.transform.scale(character1,(50,55))
character1.set_colorkey(WHITE)
character2 = pygame.image.load('swatswalkingcycle2.png')
character2= pygame.transform.scale(character2,(50,55))
character2.set_colorkey(WHITE)
#background = pygame.image.load('action cycle 3.jpg')
#background= pygame.transform.scale(background,(50,55))
Realbackground = pygame.image.load('Mbackground.png')
Realbackground= pygame.transform.scale(Realbackground,(775,500))
characterAnimationL = [character1,character2,]

