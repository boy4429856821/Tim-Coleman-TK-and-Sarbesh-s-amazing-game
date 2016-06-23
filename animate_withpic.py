import pygame as py
py.init() 
screeen = py.display.set_mode((600,600))
py.display.set_caption("Keybinding ")

white = (255,255,255)
black=(0,0,0)

class Animate:
    def _init_(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def loadImage(self,character):
        self.character1 = py.image.load(character)
        self.character1 = py.transform.scale(self.character,(width,height))
    def drawOn(self,screeen):
        screeen.blit(self.character1, (x,y))
Animate.loadImage("actioncycle1.jpg")
moveX,moveY= (0,0)

while True:
    eventLs= py.event.get()
    for event in eventLs:
        if event.type==py.QUIT:
            py.quit()
        if event.type==py.KEYDOWN:
            if event.type == py.K_LEFT:
                moveX = -4
            if event.type == py.K_RIGHT:
                moveX = 4
            if event.type == py.K_UP:
                moveY = -4
            if event.type == py.K_DOWN:
                moveY = 4
        if event.type == py.KEYUP:
            if event.type == py.K_LEFT:
                moveX = 0
            if event.type == py.K_RIGHT:
                moveX = 0
            if event.type == py.K_UP:
                moveY = 0
            if event.type == py.K_DOWN:
                moveY = 0
    screeen.fill(white)
    character1.x += moveX
    character1.y += moveY
    Animate.drawOn()
    
    py.display.flip()
py.quit()


