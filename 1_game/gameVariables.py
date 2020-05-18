#!/usr/bin/env python
import pygame
from pygame.locals import *

# global variables to initialize the game and set proper proportions

gameWidth = 300                         #Game window gameWidth
gameHeight = 500                        #Game window gameHeight
FPS = 60                                #Frames per second

birdHeight = 35                              #Height of the bird
birdWidth = 48                               #Width of the bird
jumpSteps = 15                               #Pixels to move
jumpPixels = 4                               #Pixels per frame
dropPixels = 3                               #Pixels per frame

groundHeight = 73                            #Height of the ground
pipeWidth = 52                               #Width of a pipe
pipeHeight = 320                             #Max Height of a pipe
pipesSpace = 4 * birdHeight                  #Space between pipes
pipesAddInterval = 2000                      #Milliseconds

pixelsFrame = 2                              #Pixels per frame
getNewPipe = USEREVENT + 1                   #Custom event

pygame.init()                                #Initialize pygame
screenResolution = pygame.display.Info()     #Get screen resolution
pygame.quit()                                #Close pygame

gameScore = 0                                #Game gameScore
waitClick = True
