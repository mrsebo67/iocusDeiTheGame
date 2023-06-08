from perlin_noise import PerlinNoise
import matplotlib.image
from datetime import datetime

class World():

    def __init__(self) -> None:
        pass


    def createWorld(self):
        currSec = int(datetime.now().strftime("%S"))

        noise = PerlinNoise(octaves=10, seed=currSec)
        xpix, ypix = 100, 100
        pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

        maxValue = 0

        for i in range(len(pic)):
            for j in range(len(pic[i])):
                pic[i][j] += 0.5
                pic[i][j] = int(round(abs(pic[i][j]), 2) * 100)
                if(pic[i][j] > maxValue):
                    maxValue = pic[i][j]
                
        for i in range(len(pic)):
            for j in range(len(pic[i])):
                pic[i][j] = int(( (pic[i][j]) / (maxValue - 0) ) * (5))
                #pic [i][j] = 5 - pic[i][j]



        with open('src/testing/world.txt', 'w') as f:

            for elem in pic:
                for char in elem:
                    f.write(str(char)  + " ")

                f.write("\n")
        
        matplotlib.image.imsave('src/testing/world.png', pic)


    def loadWorld(self):
        pass

    def saveWorld(self):
        pass