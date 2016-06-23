import pygame
import time
white = (255,255,255)
pygame.init()
screen = pygame.display.set_mode((1200, 700))

character1 = pygame.image.load('action cycle1.jpg')
character1= pygame.transform.scale(character1,(100,175))
character2 = pygame.image.load('action cycle2.jpg')
character2= pygame.transform.scale(character2,(100,175))
background = pygame.image.load('action cycle 3.jpg')
background= pygame.transform.scale(background,(100,175))
Realbackground = pygame.image.load('platform.png')
Realbackground= pygame.transform.scale(Realbackground,(800,300))

#background = background.convert()
#background = background.convert_alpha()

g = 1
screen.fill(white)
screen.blit(Realbackground, (0, 73))
#character1.set_colorkey((77,79,86))
#character1.set_alpha(None)
#character2.set_colorkey((77,79,86))
#character2.set_alpha(None)


while True:
    eventLs = pygame.event.get()
    for event in eventLs:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    g = (g+1)% 50
    print(g)
    if (g > 10):
        screen.blit(character1, (50, 50))
    if(g >20):
        screen.blit(character2, (50, 50))    
    if(g >30):
        screen.blit(background, (50, 50))
       
    pygame.display.flip()
    
