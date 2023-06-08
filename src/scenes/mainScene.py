import pyglet
from random import randint
from worldManipulation.world import World




class MainScene:



    def __init__(self, window) -> None:
        self.width = window.width
        self.height = window.height
        self.centerX = window.width//2
        self.centerY = window.height//2

        self.loadTextures()

        #todo if the world is present in savefiles load the world instead of creating
        self.world = World()
        self.world.createWorld()



    def loadTextures(self):
        heart = pyglet.image.load("sprites/heart.png")
        heart.anchor_x = heart.width // 2
        heart.anchor_y = heart.height // 2
        self.heartSprite = pyglet.sprite.Sprite(heart, x= self.centerX, y= self.centerY)

        mainSceneBG = pyglet.image.load("sprites/mainSceneBG.png")
        mainSceneBG.anchor_x = mainSceneBG.width // 2
        mainSceneBG.anchor_y = mainSceneBG.height // 2
        self.mainSceneBGSprite = pyglet.sprite.Sprite(mainSceneBG, x=self.centerX, y=self.centerY)

    def loadWorld(self):
        pass

    def update(self):

        self.heartSprite.update(scale=randint(1,5)*2)


    def draw(self):

        
        self.mainSceneBGSprite.draw()
        self.heartSprite.draw()


    