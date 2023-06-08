from perlin_noise import PerlinNoise
import matplotlib.image
from datetime import datetime

class World():

    def __init__(self) -> None:
        pass


    def createWorld(self):
        currSec = int(datetime.now().strftime("%S"))

        noise = PerlinNoise(octaves=4, seed=currSec)
        xpix, ypix = 100, 100
        pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]


        with open('src/testing/world.txt', 'w') as f:

            for elem in pic:
                for char in elem:
                    
                    char = str(int(round(abs(char), 2)*100)) + " "
                    f.write(char)

                f.write("\n")
        
        matplotlib.image.imsave('src/testing/world.png', pic)


    def loadWorld(self):
        pass

    def saveWorld(self):
        pass