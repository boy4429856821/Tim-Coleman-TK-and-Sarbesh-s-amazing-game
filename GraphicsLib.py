import pygame

WHITE = (255, 255, 255)
ORANGE = (255, 153, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
orange=(255,153,0)
black = (0,0,0)
red = (255,25,25)

# First Character walking cycle and shooting cycle
character1 = pygame.image.load('swatshootingcycle1.png')
character1= pygame.transform.scale(character1,(70,75))
character1.set_colorkey(WHITE)
character2 = pygame.image.load('swatswalkingcycle2.png')
character2= pygame.transform.scale(character2,(70,75))
character2.set_colorkey(WHITE)
shotsFired = pygame.image.load('swatshootingcycle2.png')
shotsFired = pygame.transform.scale(shotsFired,(70,75))
shotsFired.set_alpha()
shotsFired.set_colorkey(WHITE)
ShootingSprite =[character1,shotsFired]


#background = pygame.image.load('action cycle 3.jpg')
#background= pygame.transform.scale(background,(50,55))

# all the staring screens 
Realbackground = pygame.image.load('Mbackground.png')
Realbackground= pygame.transform.scale(Realbackground,(1250,800))
characterAnimationL = [character1,character2]
Reloadimg = pygame.image.load("Reload Image.png")
Startscreen = pygame.image.load("starting pic.png")
Startscreen = pygame.transform.scale(Startscreen,(1300,700))
Startscreen2 = pygame.image.load("ChocoBible.png")
Startscreen2 = pygame.transform.scale(Startscreen2,(1250,800))
Startscreen3 = pygame.image.load("ChocoPages.png")
Startscreen3 = pygame.transform.scale(Startscreen3,(1250,700))
Startscreen4 = pygame.image.load("ChocoCopyRight.png")
Startscreen4 = pygame.transform.scale(Startscreen4,(1250,700))
ControlScreen = pygame.image.load("ControlScreen.png")
ControlScreen = pygame.transform.scale(ControlScreen, (1250,700))
ShootingSprite = [character1,shotsFired]
GameoverS = pygame.image.load("GameOverScreen.png")
GameoverS = pygame.transform.scale(GameoverS,(1250,700))

# bullet sound 
bulletSound = pygame.mixer.Sound('BulletSound.wav')
#game music
gamesound = pygame.mixer.Sound('gamesong.wav')
# Lives
Lives = pygame.image.load("Hearts.png")
Lives = pygame.transform.scale(Lives, (35,35))
Lives.set_colorkey(WHITE)
Lives.set_alpha()

#First enemy
enemyF= pygame.image.load('dinoVillan1.png')
enemyF= pygame.transform.scale(enemyF,(60,50))
enemyF.set_colorkey(WHITE)
enemyF.set_alpha()
enemy2 = pygame.image.load('dinoVillan2.png')
enemy2= pygame.transform.scale(enemy2,(60,50))
enemy2.set_colorkey(WHITE)
enemy2.set_alpha()

# Second enemy
enemy3 = pygame.image.load("NewEnemy0.png")
enemy3 = pygame.transform.scale(enemy3,(120,100))
enemy3.set_colorkey(WHITE)
enemy3.set_alpha()
enemy32 = pygame.image.load("NewEnemy2.png")
enemy32 = pygame.transform.scale(enemy32,(120,100))
enemy32.set_colorkey(WHITE)
enemy32.set_alpha()

# "Third" enemy
enemy4 = pygame.image.load("ThirdEnemy0.png")
enemy4 = pygame.transform.scale(enemy4,(60,50))
enemy4.set_colorkey(WHITE)
enemy4.set_alpha()
enemy42 = pygame.image.load("ThirdEnemy.png")
enemy42 = pygame.transform.scale(enemy42,(60,50))
enemy42.set_colorkey(WHITE)
enemy42.set_alpha()

# Fourth  enemy
enemy5 = pygame.image.load("Pheonix0.png")
enemy5 = pygame.transform.scale(enemy5,(80,70))
enemy5.set_colorkey(WHITE)
enemy5.set_alpha()
enemy52 = pygame.image.load("Pheonix2.png")
enemy52 = pygame.transform.scale(enemy52,(80,70))
enemy52.set_colorkey(WHITE)
enemy52.set_alpha()

# Fifth enemy
enemy6 = pygame.image.load("Griffin0.png")
enemy6 = pygame.transform.scale(enemy6,(60,50))
enemy6.set_colorkey(WHITE)
enemy6.set_alpha()
enemy62 = pygame.image.load("Griffin01.png")
enemy62 = pygame.transform.scale(enemy62,(60,50))
enemy62.set_colorkey(WHITE)
enemy62.set_alpha()





# bullet animation
bullet=pygame.Surface((10,4))
pygame.draw.rect(bullet,black,(0, 0, 10, 4))
        