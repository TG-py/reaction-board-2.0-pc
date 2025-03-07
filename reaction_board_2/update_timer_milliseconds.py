import pygame
import time

def updateTimerMilliseconds(startTime, timerSurfacePos, timerFont, screen, winX, winY):
    newTime = startTime-time.time()
    screen.fill([255,255,255])
    if newTime>10: newTimeStr = str(newTime)[0:2]+":"+str(newTime)[3:5]+"0"
    else: newTimeStr = " "+str(newTime)[0]+":"+str(newTime)[2:4]+"0"
    for digit in range(5):
        if digit < 2: xOffset = (digit+1.3)/5
        else: xOffset = (digit+0.7)/5
        timerSurface, timerSurfaceRect = timerFont.render(newTimeStr[digit], [0,0,0])
        screen.blit(timerSurface, [winX*(xOffset)-timerSurfaceRect[2],winY/2-timerSurfaceRect[3]/2])
    pygame.display.flip()
    return newTime