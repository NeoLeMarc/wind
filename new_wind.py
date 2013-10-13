import pygame
import pygame.time
from pygame.locals import *
import math
import time
import sys

cache = {}
i = 0
while i <= 359:
	image = pygame.image.load("cache/screen_%i.tga" %i)
	cache[i] = image
	i += 3 
	print "Filling cache: %i" %i

clock = pygame.time.Clock()
FRAMES_PER_SECOND = 20 
deltat = clock.tick(FRAMES_PER_SECOND)

screen = pygame.display.set_mode((640, 480), FULLSCREEN)

screen.fill((0, 0, 0))
pygame.display.flip()


from weather import Weather
weather = Weather()
weather.update()
weather_info = weather.getWeatherInfo()
weather.update()

class Arrow():
    currentPosition = 0

    def setPosition(self, i):
        i = i%360
        image = cache[i] 
        screen.blit(image, (0,0))
        pygame.display.flip()
        deltat = clock.tick(FRAMES_PER_SECOND)
        self.currentPosition = i

    def moveTo(self, i):
        if abs(i -self.currentPosition) < 3:
           return False
        else:
           dir1 = (i - self.currentPosition)%360
           dir2 = (self.currentPosition - i)%360
           if (dir2 >= dir1 ):
               move_to = 3 
           else:
               move_to = -3
            
           self.setPosition(self.currentPosition + move_to)
           return True

arrow = Arrow()
tick = 0
while 1:
    if tick == 0:
        weather_info = weather.getWeatherInfo()
        weather.update()

    arrow.moveTo(int(weather_info['angle']))
    tick += 1

    if tick >= 180:
        tick = 0
