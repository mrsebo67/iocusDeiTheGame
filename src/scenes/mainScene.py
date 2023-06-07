import pyglet
from random import randint


class MainScene:



    def __init__(self, window) -> None:
        self.width = window.width
        self.height = window.height
        self.centerX = window.width//2
        self.centerY = window.height//2

        heart = pyglet.image.load("sprites/heart.png")
        heart.anchor_x = heart.width // 2
        heart.anchor_y = heart.height // 2
        self.heartSprite = pyglet.sprite.Sprite(heart, x= self.centerX, y= self.centerY)

        mainSceneBG = pyglet.image.load("sprites/mainSceneBG.png")
        mainSceneBG.anchor_x = mainSceneBG.width // 2
        mainSceneBG.anchor_y = mainSceneBG.height // 2
        self.mainSceneBGSprite = pyglet.sprite.Sprite(mainSceneBG, x=self.centerX, y=self.centerY)



    def update(self):

        self.heartSprite.x = randint(0, self.width)
        self.heartSprite.y = randint(0, self.height)


    def draw(self):

        
        self.mainSceneBGSprite.draw()
        self.heartSprite.draw()


    