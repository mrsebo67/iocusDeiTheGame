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
        heart = pyglet.image.load("src/testing/world.png")
        heart.anchor_x = heart.width // 2
        heart.anchor_y = heart.height // 2
        self.heartSprite = pyglet.sprite.Sprite(heart, x= self.centerX, y= self.centerY)
        self.heartSprite.update(scale_y=6)
        self.heartSprite.update(scale_x=8)

        mainSceneBG = pyglet.image.load("sprites/mainSceneBG.png")
        mainSceneBG.anchor_x = mainSceneBG.width // 2
        mainSceneBG.anchor_y = mainSceneBG.height // 2
        self.mainSceneBGSprite = pyglet.sprite.Sprite(mainSceneBG, x=self.centerX, y=self.centerY)
        self.mainSceneBGSprite.update(scale=1.03)

    def loadWorld(self):
        pass

    def update(self):
        pass


    def draw(self):

        
        
        self.heartSprite.draw()
        self.mainSceneBGSprite.draw()


    