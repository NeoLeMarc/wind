import pygame
import pygame.time
from pygame.locals import *
import math
import time
import sys

clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30
deltat = clock.tick(FRAMES_PER_SECOND)

screen = pygame.display.set_mode((1024, 768), DOUBLEBUF)

screen.fill((0, 0, 0))
pygame.display.flip()

class ArrowSprite(pygame.sprite.Sprite):

    def __init__(self, image, position, name):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.direction = 1
        self.target_direction = 0
        self.move_to = 1
        self.airspeed = 0
        self.image = self.src_image
        self.cache = {}
        self.has_changed = 0
        self.name = name

    def getCache(self, direction, function):
        try:
            image = pygame.image.load("cache/%s_%i.tga" % (self.name, direction))
        except:
            image = function()
            pygame.image.save(self.image, "cache/%s_%i.tga" % (self.name, direction))
        return image


    def update(self, deltat):
        if self.direction != self.target_direction:
           self.has_changed = 1
           dir1 = (self.target_direction - self.direction)%360
           dir2 = (self.direction - self.target_direction)%360
           if (dir2 > dir1 ):
               self.move_to = self.airspeed 
           else:
               self.move_to = -(self.airspeed)

           self.direction = int((self.direction + self.move_to)%360)
           self.image = self.getCache(self.direction, lambda : pygame.transform.rotate(self.src_image , self.direction))
        else:
            self.has_changed = 0

        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def setTargetDirection(self, target_direction):
        self.target_direction = int(target_direction)

    def setAirspeed(self, speed):
        self.airspeed = float(speed) + 1

    def getHasChanged(self):
        return self.has_changed

rect = screen.get_rect()
arrow = ArrowSprite("arrow.png", rect.center, "arrow")
arrow_shadow = ArrowSprite("shadow.png", rect.move(3,3).center, "shadow")
#arrow_group = pygame.sprite.RenderPlain(arrow)
arrow_group = pygame.sprite.RenderPlain(arrow, arrow_shadow)
pygame.display.flip()

def updateArrow():
    deltat = clock.tick(FRAMES_PER_SECOND)
    arrow_group.update(deltat)
    if arrow.getHasChanged():
        screen.fill((0,0,255))
        arrow_group.draw(screen)
    #pygame.display.flip()
    pygame.display.update(arrow.rect)


from weather import Weather
weather = Weather()
weather.update()

tick = 0
while 1:
    if tick == 0:
        weather_info = weather.getWeatherInfo()
        weather.update()

        arrow.setTargetDirection(weather_info['angle'])
        arrow.setAirspeed(weather_info['speed'])

        arrow_shadow.setTargetDirection(weather_info['angle'])
        arrow_shadow.setAirspeed(weather_info['speed'])

    tick += 1

    updateArrow()
    pygame.image.save(screen, "cache/screen_%i.tga" % (int(arrow.direction)))
    time.sleep(1/FRAMES_PER_SECOND)
    
    if tick >= 180:
        tick = 0
