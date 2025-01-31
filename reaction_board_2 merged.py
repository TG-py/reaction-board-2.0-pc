import pygame
import random
import time
import pygame.freetype
import pickle
import math
from gpiozero import Button, LED


#sound on button press to stop confusion on multiple presses of the same button
#lights show on buttons when not being played to draw people in
#colours on screen
#find a way to make the leaderboard experience better or remove leaderboard
#make everything intuitive to everyone
#maybe switch to number of buttons pressed in a min to make it more fun instead of competitive


def setup():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode()
    pygame.display.set_caption("screen")
    winX, winY = pygame.display.get_window_size()
    clock = pygame.time.Clock()

    with open('scores.pk', 'rb') as scoresFile:
        scores = pickle.load(scoresFile)
    highest = 0
    total = 0
    for i in scores:
        total += i
        if i > highest:
            highest = i
    avg = total/len(scores)
    playerCount = len(scores)

    return screen, winX, winY, highest, total, avg, playerCount

def gameSetup():    
    groundInPinNum = 21
    groundInPin = Button(groundInPinNum, pull_up=False)
    
    ledNums = [4, 15, 17, 22, 24, 9, 11, 7, 0, 6, 13, 16]
    leds = []
    for i in range(len(ledNums)):
        leds.append(LED(ledNums[i]))

    buttonNums = [14, 18, 27, 23, 10, 25, 8, 1, 5, 12, 19]
    buttons = []
    for i in range(len(buttonNums)):
        buttons.append(Button(buttonNums[i]))
    
    workingPins = []
    for i in range(len(leds)):
        leds[i].on()
        workingPins.append(groundInPin.is_pressed)
        leds[i].off()
    print(workingPins)
    
    groundInPin.close()
    groundInPin = LED(groundInPinNum)
    groundInPin.off()
        
    
    return groundInPinNum, groundInPin, leds, buttons, workingPins


def gameStart():
    screen.fill([255,255,255])
    font = pygame.freetype.SysFont(None, winY*0.80)
    timerSurface, timerSurfaceRect = font.render("1", [0,0,0])
    timerSurfacePos = [winX/2-timerSurfaceRect[2],winY/2-timerSurfaceRect[3]/2]
    screen.blit(timerSurface, timerSurfacePos)
    pygame.display.flip()
    return timerSurfacePos


def game(groundInPinNum, groundInPin, leds, buttons, workingPins, timerSurfacePos):
    
    buttonsPressed = 0
    startTime = time.time() + 15
    breakVar = False
    
    while True:
        buttonNum = random.randint(0, 2)
        
        groundInPin.close()
        groundInPin = Button(groundInPinNum, pull_up=False)
        
        leds[buttonNum].on()
        pinWorking = groundInPin.is_pressed
        print(pinWorking)
        leds[buttonNum].off()

        groundInPin.close()
        groundInPin = LED(groundInPinNum)
        groundInPin.off()
        
        if not pinWorking: continue
        
        
        
        leds[buttonNum].on()
        while not buttons[buttonNum].is_pressed:
            if 0 > updateTimer(startTime, timerSurfacePos):
                breakVar = True
                break
        if breakVar: break
        buttonsPressed += 1
        leds[buttonNum].off()
        while buttons[buttonNum].is_pressed:
            if 0 > updateTimer(startTime, timerSurfacePos):
                breakVar = True
                break
        if breakVar: break
    timer = updateTimer(startTime, timerSurfacePos)
    for i in leds:
        i.off()
    return buttonsPressed


def updateTimer(startTime, timerSurfacePos):
    newTime = startTime-time.time()
    screen.fill([255,255,255])
    font = pygame.freetype.SysFont(None, winY*0.70)
    if newTime>10: newTimeStr = str(newTime)[0:2]+":"+str(newTime)[3:5]+"0"
    else: newTimeStr = " "+str(newTime)[0]+":"+str(newTime)[2:4]+"0"
    for digit in range(5):
        if digit < 2: xOffset = (digit+1.3)/5
        else: xOffset = (digit+0.7)/5
        timerSurface, timerSurfaceRect = font.render(newTimeStr[digit], [0,0,0])
        screen.blit(timerSurface, [winX*(xOffset)-timerSurfaceRect[2],winY/2-timerSurfaceRect[3]/2])
    pygame.display.flip()
    return newTime


def gameFinished(buttonsPressed):
    screen.fill([255,255,255])
    youScoredFont = pygame.freetype.SysFont(None, winY*0.09)
    scoreFont = pygame.freetype.SysFont(None, winY*0.6)
    buttonFont = pygame.freetype.SysFont(None, winY*0.09)
    youScoredSurface, youScoredRect = youScoredFont.render("YOU SCORED:", [0,0,0])
    screen.blit(youScoredSurface, [winX*0.5-youScoredRect[2]/2, winY*0.1-youScoredRect[3]/2])
    scoreSurface, scoreSurfaceRect = scoreFont.render(str(buttonsPressed), [0,0,0])
    screen.blit(scoreSurface, [winX*0.5-scoreSurfaceRect[2]/2, winY*0.4-scoreSurfaceRect[3]/2])
    continueButton = pygame.draw.rect(screen, (200,200,200), [winX*0.39,winY*0.8,winX*0.22,winY*0.1], 0, round(winY*0.01))
    pygame.draw.rect(screen, (230,0,0), [winX*0.40,winY*0.81,winX*0.2,winY*0.08], 0, round(winY*0.01))
    buttonTextSurface, buttonTextSurfaceRect = buttonFont.render("OK", [0,0,0])
    screen.blit(buttonTextSurface, [winX*0.5-buttonTextSurfaceRect[2]/2, winY*0.85-buttonTextSurfaceRect[3]/2])
    pygame.display.flip()
    openScreen = time.time()
    while time.time()-openScreen < 10:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continueButton.collidepoint(event.pos[0], event.pos[1]):
                    return True
    return False


def betweenGames(highest, total, avg, playerCount):
    screen.fill([255,255,255])
    startButton = pygame.draw.rect(screen, (200,200,200), [winX*0.36,winY*0.22,winX*0.28,winY*0.16], 0, round(winY*0.01))
    pygame.draw.rect(screen, (230,0,0), [winX*0.37,winY*0.23,winX*0.26,winY*0.14], 0, round(winY*0.01))
    font = pygame.freetype.SysFont(None, winY*0.13)
    timerSurface, timerSurfaceRect = font.render("START", [0,0,0])
    screen.blit(timerSurface, [winX*0.5-timerSurfaceRect[2]/2, winY*0.3-timerSurfaceRect[3]/2])
    infoFont = pygame.freetype.SysFont(None, winY*0.1)
    highestSurface, highestRect = infoFont.render(f"THE BEST SCORE IS: {highest}", [0,0,0])
    screen.blit(highestSurface, [winX*0.5-highestRect[2]/2, winY*0.5-highestRect[3]/2])
    avgSurface, avgRect = infoFont.render(f"THE AVERAGE SCORE IS: {round(avg)}", [0,0,0])
    screen.blit(avgSurface, [winX*0.5-avgRect[2]/2, winY*0.7-avgRect[3]/2])
    playerCountSurface, playerCountRect = infoFont.render(f"{playerCount} PEOPLE HAVE PLAYED", [0,0,0])
    screen.blit(playerCountSurface, [winX*0.5-playerCountRect[2]/2, winY*0.9-playerCountRect[3]/2])
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(event.pos[0], event.pos[1]):
                    return


def otherPlayerComparison(score):
    with open('scores.pk', 'rb') as scoresFile:
        scores = pickle.load(scoresFile)
    total = 0
    highest = 0
    beatenScores = []
    place = 1
    for i in scores:
        total += i
        if highest < i:
            highest = i
        if i <= score:
            beatenScores.append(i)
        else:
            place += 1
    avg = total/len(scores)
    playerCount = len(scores)+1
    percentageBeaten = 100 - math.floor(((len(beatenScores)/len(scores))*100)-0.0000001)
    scores.append(score)
    with open('scores.pk', 'wb') as scoresFile:
        pickle.dump(scores, scoresFile)
    return percentageBeaten, place, highest, total, avg, playerCount


def showTopPercentage(percentageBeaten):
    screen.fill([255,255,255])
    topFont = pygame.freetype.SysFont(None, winY*0.09)
    percentageFont = pygame.freetype.SysFont(None, winY*0.6)
    buttonFont = pygame.freetype.SysFont(None, winY*0.09)
    topSurface, topRect = topFont.render("YOU WERE IN THE TOP:", [0,0,0])
    screen.blit(topSurface, [winX*0.5-topRect[2]/2, winY*0.1-topRect[3]/2])
    percentageSurface, percentageRect = percentageFont.render(f"{percentageBeaten}%", [0,0,0])
    screen.blit(percentageSurface, [winX*0.5-percentageRect[2]/2, winY*0.4-percentageRect[3]/2])
    continueButton = pygame.draw.rect(screen, (200,200,200), [winX*0.39,winY*0.8,winX*0.22,winY*0.1], 0, round(winY*0.01))
    pygame.draw.rect(screen, (230,0,0), [winX*0.40,winY*0.81,winX*0.2,winY*0.08], 0, round(winY*0.01))
    buttonTextSurface, buttonTextSurfaceRect = buttonFont.render("OK", [0,0,0])
    screen.blit(buttonTextSurface, [winX*0.5-buttonTextSurfaceRect[2]/2, winY*0.85-buttonTextSurfaceRect[3]/2])
    pygame.display.flip()
    openScreen = time.time()
    while time.time()-openScreen < 10:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continueButton.collidepoint(event.pos[0], event.pos[1]):
                    return True
    return False


def showPlace(place):
    screen.fill([255,255,255])
    topFont = pygame.freetype.SysFont(None, winY*0.09)
    placeFont = pygame.freetype.SysFont(None, winY*0.6)
    buttonFont = pygame.freetype.SysFont(None, winY*0.09)
    topSurface, topRect = topFont.render("YOU PLACED:", [0,0,0])
    screen.blit(topSurface, [winX*0.5-topRect[2]/2, winY*0.1-topRect[3]/2])
    if str(place)[-1] == "1":
        suffix = "st"
    elif str(place)[-1] == "2":
        suffix = "nd"
    elif str(place)[-1] == "3":
        suffix = "rd"
    else:
        suffix = "th"
    placeSurface, placeRect = placeFont.render(f"{place}{suffix}", [0,0,0])
    screen.blit(placeSurface, [winX*0.5-placeRect[2]/2, winY*0.4-placeRect[3]/2])
    continueButton = pygame.draw.rect(screen, (200,200,200), [winX*0.39,winY*0.8,winX*0.22,winY*0.1], 0, round(winY*0.01))
    pygame.draw.rect(screen, (230,0,0), [winX*0.40,winY*0.81,winX*0.2,winY*0.08], 0, round(winY*0.01))
    buttonTextSurface, buttonTextSurfaceRect = buttonFont.render("OK", [0,0,0])
    screen.blit(buttonTextSurface, [winX*0.5-buttonTextSurfaceRect[2]/2, winY*0.85-buttonTextSurfaceRect[3]/2])
    pygame.display.flip()
    openScreen = time.time()
    while time.time()-openScreen < 10:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continueButton.collidepoint(event.pos[0], event.pos[1]):
                    return True
    return False


screen, winX, winY, highest, total, avg, playerCount = setup()
groundInPinNum, groundInPin, leds, buttons, workingPins = gameSetup()
while True:
    betweenGames(highest, total, avg, playerCount)
    timerSurfacePos = gameStart()
    buttonsPressed = game(groundInPinNum, groundInPin, leds, buttons, workingPins, timerSurfacePos)
    topPercentage, place, highest, total, avg, playerCount = otherPlayerComparison(buttonsPressed)
    if gameFinished(buttonsPressed):
        if showTopPercentage(topPercentage):
            showPlace(place)