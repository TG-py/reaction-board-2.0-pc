import pygame
import time
import math

def updateTimer(startTime, timerScreens, screen):
    newTime = startTime-time.time()
    screen.blit(timerScreens[math.floor(newTime)], [0,0], timerScreens[math.floor(newTime)].get_rect())
    pygame.display.flip()
    return newTime