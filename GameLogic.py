import pygame
import GraphicsLib as GLib
from Util import *
import random


EnemyPositionList=[50,100,150,200,250,300,350,400,450,500,550,600]
# a great example of an object that can move on the screen
class enemy1():
    def __init__(self):
        self.img= GLib.enemy1
        self.lives=1
        self.x = 1225
        self.vx = -1
        self.y=EnemyPositionList[random.randint(0,len(EnemyPositionList)-1)]
    
    def update(self):
        self.x += self.vx

class Sprite:
    def __init__(self):
        # ------------------------
        # [REQUIRED PART] for any class that will be drawn on the screen
        # Grab the surface that Graphics people worked very hard on
        self.img = GLib.character1
        # Set the initial coordinate of this object
        self.x = 100
        self.y = 50
        self.pastx = self.x
        self.pasty = self.y
        # ------------------------
        # TODO: add more properties to Sprite based on your game
        self.vx = 0
        self.vy = 0
        self.lives=10

    # an example of updating position of the object
    def update(self):
        # TODO: what else Sprite is going to do in each frame
        bounceIn(self,0,0,1225,700)
        
    def MovementDetection(self):
        CharacterAnimationL = [GLib.character1]
        if self.x != self.pastx or self.y != self.pasty:
            CharacterAnimationL= GLib.characterAnimationL
        self.pastx = self.x
        self.pasty = self.y
        return CharacterAnimationL
            

# the minimum class for an object that can be displaced on the screen
class Ball:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img


class Game:
    def __init__(self):
        # initialize the timer to zero. This is like a little clock
        self.timer = 0
        self.sprite = Sprite()
        self.enemyList = []
        # self.ball = Ball(250, 250, GLib.ballSpriteBLUE)
        # TODO: add any variables you think will be needed as a property of Game
        # ...
        # ..
        # .
        # TODO: add any objects that you would like to be drawn on the screen
        # Make sure that all of those objects has x, y and img defined as their property
        self.objectsOnScreen = []
    


    # Try to update all the elements
    # if you want to add another to the screen:                 self.objectsOnScreen.add(x)
    # if you want to remove a object from the screen:           self.objectsOnScreen.remove(x)
    # if you want to switch to another the state                return 10                      --> this switches to state 10
    # if you want to bring a object to the front                
        # just remove it first and then added it back
        # the last added object is going to be on the top
    def updateInState(self, state):
        # increment the timer
        self.timer += 1
        # check what state the game is at
        if state == "Normal":
            if self.timer % 10 == 0:
                e=enemy1()
                self.enemyList.append(e)
            for e in self.enemyList:
                e.update()
                if e.x<=-50:
                    self.enemyList.remove(e)
            #elif state == "MovingLeft" :
            showAnimationOn(self.sprite, self.sprite.MovementDetection(), self.timer )
            self.sprite.update()
        elif state == "StartScreen":
            pass
        elif state == "Attack":
            showAnimationOn(self.sprite, GLib.ShootingSprite, self.timer/1)
        else:
            print("Undefined game state " + str(state))
            exit()
        # return the same state if you decided not to switch a state
        return state

    





    # A method that does all the drawing for you.
    def draw(self,state, screen):
        # The first line clear the screen
        # TODO: if you want a differnt background, 
            # you can replace the next line                     
        if state == "Normal":
            screen.blit(GLib.Realbackground, (-25, -15))
        elif state == "StartScreen":
            screen.blit(GLib.Startscreen,(0,0))
        if state == "Attack":
            screen.blit(GLib.Realbackground,(-25,-15))
        

        stack = [self.objectsOnScreen]
        while len(stack) > 0:
            objectsLs = stack.pop()
            for obj in objectsLs:
                if type(obj) is list:
                    stack.append(obj)
                else:
                    screen.blit(obj.img, (obj.x, obj.y))