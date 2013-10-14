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

#screen = pygame.display.set_mode((640, 480), FULLSCREEN)
screen = pygame.display.set_mode((640, 480))


screen.fill((0, 0, 0))
pygame.display.flip()


from weather import Weather
weather = Weather()
weather.update()
weather_info = weather.getWeatherInfo()
weather.update()

class Arrow():
    current_position = 0
    speed = 0
    target_position = 0
    target_reached = False
    swing_target = 0
    slowdown = 0
    current_slowdown = 0
    swing_direction = 1

    def setTargetPosition(self, targetPosition):
        self.target_reached = False
        self.target_position = targetPosition
        self.swing_target = targetPosition 
        self.slowdown = 0

    def setPosition(self, i):
        if self.slowdown > 0:
            #print "slowdown: %i - %i" % (self.slowdown, self.current_slowdown)
            self.current_slowdown -= 1
            if self.current_slowdown < 1:
                self.current_slowdown = self.slowdown
            else:
                return

        i = i%360
        image = cache[i] 
        screen.blit(image, (0,0))
        pygame.display.flip()
        self.current_position = i
        if self.current_position == self.target_position:
            self.target_reached = True

    def swing(self):
        if self.current_position == self.swing_target:
            self.swing_direction *= -1
            self.swing_target = (self.target_position + (self.swing_direction * 12))%360
            print self.swing_target
        else:
            delta = 3 * (1 + round(self.getSpeedRange() / 8))
            self.slowdown = (32/self.getSpeedRange())

            dir1 = (self.swing_target - self.current_position)%360
            dir2 = (self.current_position - self.swing_target)%360
            if (dir2 <= dir1):
                delta *= -1 

            self.setPosition(self.current_position + delta)

    def getSpeedRange(self):
        if self.speed == 0:
            return 1
        elif self.speed < 2.5:
            return 2 
        elif self.speed < 5:
            return 4 
        elif self.speed < 10:
            return 8 
        elif self.speed < 14:
            return 16 
        else: 
            return 32 

    def moveTo(self, i):
        if not self.target_reached:
            if abs(i -self.current_position) < 3:
                self.target_reached = True
            else:
               dir1 = (i - self.current_position)%360
               dir2 = (self.current_position - i)%360
               if (dir2 >= dir1 ):
                   move_to = 3 
               else:
                   move_to = -3
                
               self.setPosition(self.current_position + move_to)
               return True
        else:
           self.swing() 


arrow = Arrow()
tick = 0
while 1:
    deltat = clock.tick(FRAMES_PER_SECOND)
    if tick == 0:
        weather_info = weather.getWeatherInfo()
        weather.update()
        arrow.setTargetPosition(int(weather_info['angle']))
        arrow.speed = float(weather_info['speed'])
        speed = (float(weather_info['speed']))
        kmh = speed * 3.6
        print "Speed is currently: %f m/s (%f km/h)" % (speed, kmh)

    arrow.moveTo(int(weather_info['angle']))
    tick += 1

    if tick >= 180:
        tick = 0
