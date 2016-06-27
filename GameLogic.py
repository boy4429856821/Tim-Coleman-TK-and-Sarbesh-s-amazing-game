import pygame
import GraphicsLib as GLib
from Util import *
import random
SECSPERPOINT=18

EnemyPositionList=[50,100,150,200,250,300,350,400,450,500,550,600]
# a great example of an object that can move on the screen
class Score:
    def __init__(self):
        self.update(0)
        self.x = 1095
        self.y = 5
        
    def update(self,scoreNum):
        myfont=pygame.font.SysFont('Calibri',40,bold=True)
        self.img=myfont.render(str(scoreNum),1,GLib.RED)
<<<<<<< HEAD
           
=======
        
        
>>>>>>> origin/master
class Ammo:
    def __init__(self):
        self.update(20)
        self.x=10
        self.y=5
        
    def update(self,bulletNum):
        myfont=pygame.font.SysFont('Calibri',20,bold=True)
        self.img=myfont.render("Ammo:"+str(bulletNum),1,GLib.BLACK)

class enemy1():
    def __init__(self):
        self.enemyAnim = [GLib.enemyF,GLib.enemy2]
        self.img = GLib.enemyF
        self.x = 1225
        self.vx = -1
        self.y=EnemyPositionList[random.randint(0,len(EnemyPositionList)-1)]
        self.t =0
    def update(self):
        self.x += self.vx
        self.img = self.enemyAnim[(self.t // 2 )% 2] 
        self.t = self.t + 1
    
        
class Bullet:
# self.sprite.x , self.sprite.y
    def __init__(self, x, y): 
        self.x=x-3
        self.y=y+19
        self.img=GLib.bullet
        
    def update(self):
        self.x += 35
        
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
        self.lives=5
        self.bullets=20
    

    # an example of updating position of the object
    def update(self):
        # TODO: what else Sprite is going to do in each frame
        bounceIn(self, 0, 0, 1225, 700)
        
    def MovementDetection(self):
        CharacterAnimationL = [GLib.character1]
        if self.x != self.pastx or self.y != self.pasty:
            CharacterAnimationL= GLib.characterAnimationL
        self.pastx = self.x
        self.pasty = self.y
        return CharacterAnimationL
                    

# the minimum class for an object that can be displaced on the screen



class Game:
    def __init__(self):
        # initialize the timer to zero. This is like a little clock
        self.timer = 0
        self.sprite = Sprite()
        self.enemyList = []
        self.bulletList=[]
        self.score = Score()
        self.ammo=Ammo()
        self.LastBulletShot=0
        self.reloadTimer=0
        self.Lives= 5
        # self.ball = Ball(250, 250, GLib.ballSpriteBLUE)
        # TODO: add any variables you think will be needed as a property of Game
        # ...
        # ..
        # .
        # TODO: add any objects that you would like to be drawn on the screen
        # Make sure that all of those objects has x, y and img defined as their property
        


        #self.objectsOnScreen = [self.enemyList, self.bulletList, self.score, self.ammo, self.sprite]
        self.objectsOnScreen = []

    


    def shoot(self):

        if self.timer-self.LastBulletShot>10 and self.sprite.bullets>0:
            self.bulletList.append(Bullet(self.sprite.x , self.sprite.y ))
            self.LastBulletShot=self.timer
            self.sprite.bullets-=1

    # Try to update all the elements
    # if you want to add another to the screen:                 self.objectsOnScreen.add(x)
    # if you want to remove a object from the screen:           self.objectsOnScreen.remove(x)
    # if you want to switch to another the state                return 10                      --> this switches to state 10
    # if you want to bring a object to the front                
        # just remove it first and then added it back
        # the last added object is going to be on the top
    def updateInState(self, state):
        # increment the timer
        
        # check what state the game is at
        if state == "Normal" or state == "Attack":
            self.timer += 1
            if self.timer % 10 == 0:
                e=enemy1()
                self.enemyList.append(e)
            for e in self.enemyList:
                e.update()
                if e.x<=-50:
                    self.enemyList.remove(e)
            for i in self.bulletList:
                i.update()
                if i.x>=1200:
                   self.bulletList.remove(i)
            self.score.update(self.timer//SECSPERPOINT)
            self.ammo.update(self.sprite.bullets)
            if self.reloadTimer==self.timer:
                self.sprite.bullets=20
            for i in self.bulletList:
                for e in self.enemyList:
                    if hasCollideRect(i, e):
                        self.bulletList.remove(i)
                        self.enemyList.remove(e)
                        break
            for e in self.enemyList:
                if hasCollideRect(self.sprite, e):
                    self.Lives -= 1
            if self.Lives == 0:
                self.objectsOnScreen =[]
                return "Died"
            if state == "Normal":
                showAnimationOn(self.sprite, self.sprite.MovementDetection(), self.timer )
            else:
                showAnimationOn(self.sprite, GLib.ShootingSprite, self.timer/2)
            self.sprite.update()
        elif state == "Startscreen2":
            pass
        elif state == "Startscreen3":
            pass
        elif state == "Startscreen4":
            pass
        elif state == "Startscreen":
            pass
        elif state == "ControlScreen":
            pass
        elif state == "Died":
            pass
            
        
        
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
            screen.blit(GLib.Lives,(100,5))
            myfont=pygame.font.SysFont('Calibri',20,bold=True)
            img=myfont.render(str(self.Lives),1,GLib.WHITE)
            screen.blit(img,(100,5))
        elif state == "Startscreen2":
            screen.blit(GLib.Startscreen2,(0,0))
        elif state == "Startscreen3":
            screen.blit(GLib.Startscreen3,(0,0))
        elif state == "Startscreen4":
            screen.blit(GLib.Startscreen4,(0,0))
        elif state == "Startscreen":
            screen.blit(GLib.Startscreen,(0,0))
        elif state == "ControlScreen":
            screen.blit(GLib.ControlScreen,(0,0))
        if state == "Attack":
            screen.blit(GLib.Realbackground,(-25,-15))
        if state == "Died":
            screen.fill(GLib.BLACK)
        


        for obj in self.objectsOnScreen:
            if type(obj) is list:
                for i in obj:
                    screen.blit(i.img, (i.x, i.y))
            else:
                screen.blit(obj.img, (obj.x, obj.y))
        if state == "StartScreen":
            screen.blit(GLib.Startscreen,(0,0))