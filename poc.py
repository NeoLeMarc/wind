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
FRAMES_PER_SECOND = 8 
deltat = clock.tick(FRAMES_PER_SECOND)

screen = pygame.display.set_mode((1024, 768), FULLSCREEN)

screen.fill((0, 0, 0))
pygame.display.flip()

while 1:
    print clock.get_fps() 
    i = 0
    while i <= 359:
        image = cache[i] 
        screen.blit(image, (0,0))
        pygame.display.flip()
        deltat = clock.tick(FRAMES_PER_SECOND)
	i += 3 
