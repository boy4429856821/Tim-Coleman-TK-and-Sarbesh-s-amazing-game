import pygame
import time
white = (255,255,255)
pygame.init()
screen = pygame.display.set_mode((1200, 700))

character1 = pygame.image.load('dinoVillan1.png')
character1= pygame.transform.scale(character1,(100,175))
character2 = pygame.image.load('dinoVillan2.png')
character2= pygame.transform.scale(character2,(100,175))


g = 1
screen.fill(white)
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
       
    pygame.display.flip()
    
