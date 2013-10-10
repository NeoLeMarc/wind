import pygame
import pygame.time
from pygame.locals import *
import math

clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30
deltat = clock.tick(FRAMES_PER_SECOND)

screen = pygame.display.set_mode((1024, 768), DOUBLEBUF)

arrow = pygame.image.load('arrow.png')
screen.blit(arrow, (50, 100))
pygame.display.flip()

raw_input()

screen.fill((0, 0, 0))
rotated = pygame.transform.rotate(arrow,  90)
screen.blit(rotated, (50, 100))
pygame.display.flip()

raw_input()

screen.fill((0, 0, 0))
pygame.display.flip()

class ArrowSprite(pygame.sprite.Sprite):

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.position = position
        self.direction = 0

    def update(self, deltat):
        self.direction = (self.direction + 1)%360
        self.image = pygame.transform.rotate(self.src_image , self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

rect = screen.get_rect()
arrow = ArrowSprite("arrow.png", rect.center)
arrow_group = pygame.sprite.RenderPlain(arrow)

while 1:
    deltat = clock.tick(30)
    screen.fill((0,0,255))
    arrow_group.update(deltat)
    arrow_group.draw(screen)
    pygame.display.flip()
