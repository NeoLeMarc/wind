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
        self.direction = 0
        self.target_direction = 0
        self.move_to = 1

    def update(self, deltat):
        if self.direction != self.target_direction:
           if ( (self.direction - self.target_direction) < 0 ):
               self.move_to = 1
           else:
               self.move_to = -1

           self.direction = (self.direction + self.move_to)%360
           self.image = pygame.transform.rotate(self.src_image , self.direction)
           print "Current: %s  - Target: %s" % (self.direction, self.target_direction)

        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def setTargetDirection(self, target_direction):
        self.target_direction = int(target_direction)

rect = screen.get_rect()
arrow = ArrowSprite("arrow.png", rect.center)
arrow_group = pygame.sprite.RenderPlain(arrow)

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
    updateArrow()
    
    if tick >= 180:
        tick = 0
