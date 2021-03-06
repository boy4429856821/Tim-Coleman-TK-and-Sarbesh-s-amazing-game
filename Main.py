#-------------------------
# initialize pygame
#-------------------------
import pygame
import pygame.mixer
# initialize pygame
pygame.init()
pygame.mixer.init()

# create a screen of 500 * 500
# TODO: change the size of the screen to your design
screen = pygame.display.set_mode((1200, 700))

# <<ADVANCED>> If you want KEYDOWN event to fire continuously, when a key is held down
# ============ give it two argument, both of them are interval of KEYDOWN event
pygame.key.set_repeat(50, 50)


#-------------------------
# initialize the game
#-------------------------
## GameLogic should contain all the classes like Hero, Ball, Ship etc.
from GameLogic import *

# acquire a game object
game = Game()
sprite = Sprite()

# Let state1 be the initial state
state = "Startscreen2"
GLib.gamesound.play(-1)
EEvariable=0
EEvariable2=0

#-------------------------
# Our Main Loop
#-------------------------
## Your must have one and only one big while loop for your game
## Each time the loop is executed, one framed
while True:
    #-------------------------
    # Our event hanlding loop
    #-------------------------
    ## You are not supposed to call any graphics method like blit or flip here,
    ## All you need to do is update some state of game.
    eventList = pygame.event.get()
    # grab all events pygame recieved
    for event in eventList:
        if event.type == pygame.QUIT:
            # if someone tries to close the Windows
            exit()
  # TODO: replace the reset with your designed input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                game.sprite.x += -20
              

            if event.key == pygame.K_d:
                game.sprite.x += 20
          
                
                #state = "MovingLeft"            
            if event.key == pygame.K_w:
                game.sprite.y += -20
            if event.key == pygame.K_s:
                game.sprite.y += 20
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                exit()
            if event.key == pygame.K_LEFT:
                game.sprite.x += -20
              
            if event.key == pygame.K_r:
                game.reloadTimer=game.timer+40

            if event.key == pygame.K_RIGHT:
                game.sprite.x += 20
        
        #Easter Egg
            if event.key == pygame.K_f and state == "Startscreen":
                EEvariable=10
            if event.key == pygame.K_r and EEvariable == 10 and state == "Startscreen":
                EEvariable=20
            if event.key == pygame.K_e and EEvariable == 20 and state == "Startscreen":
                EEvariable=30
            if event.key == pygame.K_d and EEvariable == 30 and state == "Startscreen":
                game.Lives=99999999
                
                #state = "MovingLeft"            
            if event.key == pygame.K_UP:
                game.sprite.y += -20
            if event.key == pygame.K_DOWN:
                game.sprite.y += 20
            if event.key == pygame.K_SPACE:
              
                if state != "Died" :
                 state = "Attack"
                 game.shoot()
                 GLib.bulletSound.play()
                 game.objectsOnScreen = [game.enemyList, game.enemy2List, game.enemy3List, game.enemy4List, game.enemy5List, game.bulletList, game.score, game.ammo, game.sprite, game.damagetext]

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                game.sprite.x += 0
            if event.key == pygame.K_RIGHT:
                if state != "Died":
                    state = "Normal"
                game.sprite.x += 0
            if event.key == pygame.K_UP:
                game.sprite.y += 0
            if event.key == pygame.K_DOWN:
                game.sprite.y += 0
            if event.key == pygame.K_SPACE:
                if state != "Died":
                    state = "Normal"
        if event.type== pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if state == "Startscreen2":
                game.objectsOnScreen = []
                state=  "Startscreen3"
            elif state == "Startscreen3":
                game.objectsOnScreen = []
                state  ="Startscreen4"
            elif state == "Startscreen4":
                game.objectsOnScreen = []
                state ="Startscreen"
            elif state == "Startscreen":
                game.objectsOnScreen = []
                state = "ControlScreen"
            elif state == "ControlScreen":
                state = "ControlScreen"

                game.objectsOnScreen = [game.enemyList, game.enemy2List, game.enemy3List, game.enemy4List, game.enemy5List, game.bulletList, game.score, game.ammo, game.sprite, game.damagetext]

                state= "Normal"
            elif state == "Died":
                game = Game()
                state= "Startscreen"
               # game.objectsOnScreen = [game.enemyList, game.enemy2List, game.enemy3List, game.bulletList, game.score, game.ammo, game.sprite, game.damagetext]
              
    #-------------------------
    # The main game logic block
    #-------------------------
    ## all the exciting interactive of objects happen here
    ## game.updateInState() will return the next state
    state = game.updateInState(state)

    #-------------------------
    # The graphics block
    #-------------------------
    game.draw(state, screen)

    #-------------------------
    # display this frame and 
    #-------------------------
    
    pygame.display.flip()
    # ask pygame to display everythong on the GUI
    pygame.time.wait(1)
    # delay the time, so can see the Windows, controls the frame rate 