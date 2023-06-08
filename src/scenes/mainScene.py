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
        self.initWorld()

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

        mainSceneBG = pyglet.image.load("sprites/mainSceneBG2.png")
        mainSceneBG.anchor_x = mainSceneBG.width // 2
        mainSceneBG.anchor_y = mainSceneBG.height // 2
        self.mainSceneBGSprite = pyglet.sprite.Sprite(mainSceneBG, x=self.centerX, y=self.centerY)

        self.testTile = pyglet.image.load("sprites/waterTile.png")
        self.testTileSprite = pyglet.sprite.Sprite(self.testTile, x = self.centerX - 416, y=self.centerY - 316)
        self.testTileSprite2 = pyglet.sprite.Sprite(self.testTile, x=self.centerX + 400, y=self.centerY+300)
        print((self.centerX+400)-(self.centerX-416))
        print((self.centerY+300)-(self.centerY-316))
        
    def initWorld(self):

        self.sprites = [[0 for x in range(38)] for y in range(51)]

        for i in range(0, 51):
            for j in range(0, 38):
                self.sprites[i][j] = pyglet.sprite.Sprite(self.testTile, x = self.centerX - 408 + i*16, y = self.centerY - 308 + j*16)

    def renderWorld(self):

        batch = pyglet.graphics.Batch()

        for elem in self.sprites:
            for sprite in elem:
                sprite.batch=batch
        
        batch.draw()
        
        

    def loadWorld(self):
        pass

    def update(self):
        pass


    def draw(self):

        pass
        
        #self.heartSprite.draw()
        self.renderWorld()
        self.mainSceneBGSprite.draw()
        #self.testTileSprite.draw()
        #self.testTileSprite2.draw()

        


    