#-------------------------
# initialize pygame
#-------------------------
import pygame
# initialize pygame
pygame.init()

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

# Let state1 be the initial state
state = "Normal"

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
            
            if event.key == pygame.K_LEFT:
                game.hero.x += -20
                print("ok")
            if event.key == pygame.K_RIGHT:
                game.hero.x += 2
                state = "MovingLeft"            
            if event.key == pygame.K_UP:
                game.hero.y += -20
            if event.key == pygame.K_DOWN:
                game.hero.y += 20
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                game.hero.x += 0
            if event.key == pygame.K_RIGHT:
                state = "Normal"
                game.hero.x += 0
            if event.key == pygame.K_UP:
                game.hero.y += 0
            if event.key == pygame.K_DOWN:
                game.hero.y += 0

    #-------------------------
    # The main game logic block
    #-------------------------
    ## all the exciting interactive of objects happen here
    ## game.updateInState() will return the next state
    state = game.updateInState(state)

    #-------------------------
    # The graphics block
    #-------------------------
    game.draw(screen)

    #-------------------------
    # display this frame and 
    #-------------------------
    
    pygame.display.flip()
    # ask pygame to display everythong on the GUI
    pygame.time.wait(100)
    # delay the time, so can see the Windows, controls the frame rate