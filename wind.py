import pygame
import pygame.time
from pygame.locals import *
import math

clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30
deltat = clock.tick(FRAMES_PER_SECOND)

screen = pygame.display.set_mode((1024, 768), DOUBLEBUF)

screen.fill((0, 0, 0))
pygame.display.flip()

class ArrowSprite(pygame.sprite.Sprite):

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.direction = 1
        self.target_direction = 0
        self.move_to = 1
        self.airspeed = 0
        self.image = self.src_image

    def update(self, deltat):
        if self.direction != self.target_direction:
           dir1 = (self.target_direction - self.direction)%360
           dir2 = (self.direction - self.target_direction)%360
           print "%s %s" % (dir1, dir2)
           if (dir2 > dir1 ):
               self.move_to = self.airspeed + 0.1
           else:
               self.move_to = -(self.airspeed + 0.1)

           self.direction = (self.direction + self.move_to)%360
           self.image = pygame.transform.rotate(self.src_image , self.direction)
           print "Current: %s  - Target: %s - Speed: %s" % (self.direction, self.target_direction, self.airspeed)

        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def setTargetDirection(self, target_direction):
        self.target_direction = int(target_direction)

    def setAirspeed(self, speed):
        self.airspeed = float(speed) + 0.100001

rect = screen.get_rect()
arrow = ArrowSprite("arrow.png", rect.center)
arrow_shadow = ArrowSprite("shadow.png", rect.move(3,3).center)
arrow_group = pygame.sprite.RenderPlain(arrow, arrow_shadow)


def updateArrow():
    deltat = clock.tick(30)
    screen.fill((0,0,255))
    arrow_group.update(deltat)
    arrow_group.draw(screen)
    pygame.display.flip()


from weather import Weather
weather = Weather()
weather.update()

tick = 0
while 1:
    if tick == 0:
        weather_info = weather.getWeatherInfo()
        weather.update()

    tick += 1

    arrow.setTargetDirection(weather_info['angle'])
    arrow.setAirspeed(weather_info['speed'])

    arrow_shadow.setTargetDirection(weather_info['angle'])
    arrow_shadow.setAirspeed(weather_info['speed'])
    updateArrow()
    
    if tick >= 180:
        tick = 0
