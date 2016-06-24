import pygame
import time
import random
EnemyPositionList=[50,100,150,200,250,300,350,400,450,500,550,600]

orange=(255,153,0)
black = (0,0,0)
red = (255,25,25)



class enemy1():
    def __init__(self):
        self.esurface=pygame.Surface((50,50))
        pygame.draw.circle(self.esurface,orange,(25,25),25)
        self.lives=1
        self.x = 1225
        self.y=EnemyPositionList[random.randint(0,len(EnemyPositionList)-1)]
    
    def draw(self,screen):
        screen.blit(self.esurface, (self.x ,self.y))

        
pygame.init()
 
screen = pygame.display.set_mode((1200,700))
 
pygame.display.set_caption("please")

 
clock = pygame.time.Clock()
 
class Sprite:
 
    def __init__(self,x,y,width,height):
 
        self.x=x
 
        self.y=y
 
        self.width=width
 
        self.height=height

        self.lives=10
 
    def draw(self,screen):
 
        pygame.draw.rect(screen,red,(self.x,self.y,self.width,self.height))
 
Sprite1=Sprite(100,50,100,100)

moveX,moveY=0,0

EnemyList=[]
vx=-1
x=1225
y=EnemyPositionList[random.randint(0,len(EnemyPositionList)-1)]
vy=0
timer=2


gameLoop=True
while gameLoop:
 
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            exit()
 
        if (event.type==pygame.QUIT):
 
            gameLoop=False
 
        if (event.type==pygame.KEYDOWN):
 
            if (event.key==pygame.K_LEFT):
 
                moveX = -4
 
            if (event.key==pygame.K_RIGHT):
 
                moveX = 4
 
            if (event.key==pygame.K_UP):
 
                moveY = -4
 
            if (event.key==pygame.K_DOWN):
 
                moveY = 4
 
        if (event.type==pygame.KEYUP):
 
            if (event.key==pygame.K_LEFT):
 
                moveX=0
 
            if (event.key==pygame.K_RIGHT):
 
                moveX=0
 
            if (event.key==pygame.K_UP):
 
                moveY=0
 
            if (event.key==pygame.K_DOWN):
 
                moveY=0
                
            
                
 
    screen.fill(black)
    timer+=1
            
    x += vx
    y += vy
    if timer % 100 == 0:
        e=enemy1()
        EnemyList.append(e)
    for e in EnemyList:
        e.x += vx
        e.draw(screen)
        if e.x<=-50:
            EnemyList.remove(e)
    Sprite1.draw(screen)    
            
    pygame.display.flip()
    pygame.time.wait(5)


 
    Sprite1.x+=moveX
 
    Sprite1.y+=moveY
 
    Sprite1.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(50)
 



def run():
    EnemyList=[]
    vx=-1
    x=1225
    y=EnemyPositionList[random.randint(0,len(EnemyPositionList)-1)]
    vy=0
    timer=0



