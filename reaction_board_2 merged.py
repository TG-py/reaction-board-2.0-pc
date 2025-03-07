import pygame
import random
import time
import pygame.freetype
import pickle
import math
from gpiozero import Button, LED


#sound on button press to stop confusion on multiple presses of the same button
#lights show on buttons when not being played to draw people in


def setup():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
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
    gameTime = 30
    realBoard = False

    return screen, winX, winY, highest, total, avg, playerCount, gameTime, realBoard


def loading():
    screen.fill([255,255,255])
    pygame.display.flip()


def preRender(gameTime):
    #game screen render
    gameScreen = pygame.Surface(screen.get_size())
    gameScreen.fill([255,255,255])
    font = pygame.freetype.SysFont(None, winY*0.80)
    timerSurface, timerSurfaceRect = font.render("1", [0,0,0])
    timerSurfacePos = [winX/2-timerSurfaceRect[2],winY/2-timerSurfaceRect[3]/2]
    gameScreen.blit(timerSurface, timerSurfacePos)

    #timer font render
    timerFont = pygame.freetype.SysFont(None, winY*0.70)
    timerScreens = []
    for i in range(gameTime):
        timerScreens.append(pygame.Surface(screen.get_size()))
        timerScreens[i].fill([255,255,255])
        if i>=10: newTimeStr = str(i)[0:2]
        else: newTimeStr = " "+str(i)[0]
        timerSurface, timerSurfaceRect = timerFont.render(newTimeStr, [0,0,0])
        timerScreens[i].blit(timerSurface, [winX*(0.5)-timerSurfaceRect[2]/2,winY/2-timerSurfaceRect[3]/2])


    #you scored screen render
    youScoredScreen = pygame.Surface(screen.get_size())
    youScoredScreen.fill([255,255,255])
    youScoredFont = pygame.freetype.SysFont(None, winY*0.09)
    scoreFont = pygame.freetype.SysFont(None, winY*0.6)
    buttonFont = pygame.freetype.SysFont(None, winY*0.09)
    youScoredSurface, youScoredRect = youScoredFont.render("YOU SCORED:", [0,0,0])
    youScoredScreen.blit(youScoredSurface, [winX*0.5-youScoredRect[2]/2, winY*0.1-youScoredRect[3]/2])
    youScoredScreenContinueButton = pygame.draw.rect(youScoredScreen, (200,200,200), [winX*0.39,winY*0.8,winX*0.22,winY*0.1], 0, round(winY*0.01))
    pygame.draw.rect(youScoredScreen, (230,0,0), [winX*0.40,winY*0.81,winX*0.2,winY*0.08], 0, round(winY*0.01))
    buttonTextSurface, buttonTextSurfaceRect = buttonFont.render("OK", [0,0,0])
    youScoredScreen.blit(buttonTextSurface, [winX*0.5-buttonTextSurfaceRect[2]/2, winY*0.85-buttonTextSurfaceRect[3]/2])

    #between games screen render
    betweenGamesScreen = pygame.Surface(screen.get_size())
    betweenGamesScreen.fill([255,255,255])
    startButton = pygame.draw.rect(betweenGamesScreen, (200,200,200), [winX*0.36,winY*0.22,winX*0.28,winY*0.16], 0, round(winY*0.01))
    pygame.draw.rect(betweenGamesScreen, (230,0,0), [winX*0.37,winY*0.23,winX*0.26,winY*0.14], 0, round(winY*0.01))
    font = pygame.freetype.SysFont(None, winY*0.13)
    timerSurface, timerSurfaceRect = font.render("START", [0,0,0])
    betweenGamesScreen.blit(timerSurface, [winX*0.5-timerSurfaceRect[2]/2, winY*0.3-timerSurfaceRect[3]/2])
    infoFont = pygame.freetype.SysFont(None, winY*0.1)

    #show top percentage screen render
    showTopPercentageScreen = pygame.Surface(screen.get_size())
    showTopPercentageScreen.fill([255,255,255])
    topFont = pygame.freetype.SysFont(None, winY*0.09)
    percentageFont = pygame.freetype.SysFont(None, winY*0.6)
    buttonFont = pygame.freetype.SysFont(None, winY*0.09)
    topSurface, topRect = topFont.render("YOU WERE IN THE TOP:", [0,0,0])
    showTopPercentageScreen.blit(topSurface, [winX*0.5-topRect[2]/2, winY*0.1-topRect[3]/2])
    showTopPercentageContinueButton = pygame.draw.rect(showTopPercentageScreen, (200,200,200), [winX*0.39,winY*0.8,winX*0.22,winY*0.1], 0, round(winY*0.01))
    pygame.draw.rect(showTopPercentageScreen, (230,0,0), [winX*0.40,winY*0.81,winX*0.2,winY*0.08], 0, round(winY*0.01))
    buttonTextSurface, buttonTextSurfaceRect = buttonFont.render("OK", [0,0,0])
    showTopPercentageScreen.blit(buttonTextSurface, [winX*0.5-buttonTextSurfaceRect[2]/2, winY*0.85-buttonTextSurfaceRect[3]/2])

    #place screen render
    placeScreen = pygame.Surface(screen.get_size())
    placeScreen.fill([255,255,255])
    topFont = pygame.freetype.SysFont(None, winY*0.09)
    placeFont = pygame.freetype.SysFont(None, winY*0.6)
    buttonFont = pygame.freetype.SysFont(None, winY*0.09)
    topSurface, topRect = topFont.render("YOU PLACED:", [0,0,0])
    placeScreen.blit(topSurface, [winX*0.5-topRect[2]/2, winY*0.1-topRect[3]/2])
    placeScreenContinueButton = pygame.draw.rect(placeScreen, (200,200,200), [winX*0.39,winY*0.8,winX*0.22,winY*0.1], 0, round(winY*0.01))
    pygame.draw.rect(placeScreen, (230,0,0), [winX*0.40,winY*0.81,winX*0.2,winY*0.08], 0, round(winY*0.01))
    buttonTextSurface, buttonTextSurfaceRect = buttonFont.render("OK", [0,0,0])
    placeScreen.blit(buttonTextSurface, [winX*0.5-buttonTextSurfaceRect[2]/2, winY*0.85-buttonTextSurfaceRect[3]/2])

    return (gameScreen,
            timerScreens,
            [youScoredScreen, scoreFont, youScoredScreenContinueButton],
            [betweenGamesScreen, infoFont, startButton],
            [showTopPercentageScreen, percentageFont, showTopPercentageContinueButton],
            [placeScreen, placeFont, placeScreenContinueButton])


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
    workingPinsNum = 0
    for i in range(len(leds)):
        leds[i].on()
        workingPins.append(groundInPin.is_pressed)
        if groundInPin.is_pressed: workingPinsNum += 1
        leds[i].off()
    
    groundInPin.close()
    groundInPin = LED(groundInPinNum)
    groundInPin.off()
        
    
    return groundInPinNum, groundInPin, leds, buttons, workingPins, workingPinsNum


def gameStart(gameScreen):
    screen.blit(gameScreen, [0,0], gameScreen.get_rect())


def game(groundInPinNum, groundInPin, leds, buttons, workingPins, workingPinsNum, timerScreens):
    
    buttonsPressed = 0
    startTime = time.time() + gameTime
    breakVar = False
    
    while True:
        buttonNum = random.randint(0, workingPinsNum)
        k = 0

        for i in range(len(workingPins)):
            if workingPins[i]: k+=1
            if k == buttonNum:
                buttonNum = i
        
        groundInPin.close()
        groundInPin = Button(groundInPinNum, pull_up=False)
        
        leds[buttonNum].on()
        pinWorking = groundInPin.is_pressed
        leds[buttonNum].off()

        groundInPin.close()
        groundInPin = LED(groundInPinNum)
        groundInPin.off()
        
        if not pinWorking: continue
        
        
        
        leds[buttonNum].on()
        while not realBoardSwitch(buttons[buttonNum].is_pressed):
            if 0 > updateTimer(startTime, timerScreens):
                breakVar = True
                break
        if breakVar: break
        buttonsPressed += 1
        leds[buttonNum].off()
        while realBoardSwitch(buttons[buttonNum].is_pressed):
            if 0 > updateTimer(startTime, timerScreens):
                breakVar = True
                break
        if breakVar: break
    timer = updateTimer(startTime, timerScreens)
    for i in leds:
        i.off()
    return buttonsPressed


def realBoardSwitch(inputVar):
    if realBoard: return not inputVar
    else: return inputVar


def updateTimerMilliseconds(startTime, timerSurfacePos, timerFont):
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

def updateTimer(startTime, timerScreens):
    newTime = startTime-time.time()
    screen.blit(timerScreens[math.floor(newTime)], [0,0], timerScreens[math.floor(newTime)].get_rect())
    pygame.display.flip()
    return newTime


def gameFinished(buttonsPressed, youScoredScreen, scoreFont, continueButton):
    screen.blit(youScoredScreen, [0,0], youScoredScreen.get_rect())
    scoreSurface, scoreSurfaceRect = scoreFont.render(str(buttonsPressed), [0,0,0])
    screen.blit(scoreSurface, [winX*0.5-scoreSurfaceRect[2]/2, winY*0.4-scoreSurfaceRect[3]/2])
    pygame.display.flip()
    openScreen = time.time()
    while time.time()-openScreen < 10:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continueButton.collidepoint(event.pos[0], event.pos[1]):
                    return True
    return False


def betweenGames(highest, total, avg, playerCount, betweenGamesScreen, infoFont, startButton):
    screen.blit(betweenGamesScreen, [0,0], betweenGamesScreen.get_rect())
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


def showTopPercentage(percentageBeaten, showTopPercentageScreen, percentageFont, continueButton):
    screen.blit(showTopPercentageScreen, [0,0], showTopPercentageScreen.get_rect())
    percentageSurface, percentageRect = percentageFont.render(f"{percentageBeaten}%", [0,0,0])
    screen.blit(percentageSurface, [winX*0.5-percentageRect[2]/2, winY*0.4-percentageRect[3]/2])
    pygame.display.flip()
    openScreen = time.time()
    while time.time()-openScreen < 10:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continueButton.collidepoint(event.pos[0], event.pos[1]):
                    return True
    return False


def showPlace(place, placeScreen, placeFont, continueButton):
    if str(place)[-1] == "1":
        suffix = "st"
    elif str(place)[-1] == "2":
        suffix = "nd"
    elif str(place)[-1] == "3":
        suffix = "rd"
    else:
        suffix = "th"
    screen.blit(placeScreen, [0,0], placeScreen.get_rect())
    placeSurface, placeRect = placeFont.render(f"{place}{suffix}", [0,0,0])
    screen.blit(placeSurface, [winX*0.5-placeRect[2]/2, winY*0.4-placeRect[3]/2])
    pygame.display.flip()
    openScreen = time.time()
    while time.time()-openScreen < 10:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if continueButton.collidepoint(event.pos[0], event.pos[1]):
                    return True
    return False


screen, winX, winY, highest, total, avg, playerCount, gameTime, realBoard = setup()
loading()
groundInPinNum, groundInPin, leds, buttons, workingPins, workingPinsNum = gameSetup()
gameScreen, timerScreens, youScoredScreen, betweenGamesScreen, showPercentageScreen, placeScreen = preRender(gameTime)
while True:
    betweenGames(highest, total, avg, playerCount, *betweenGamesScreen)
    gameStart(gameScreen)
    buttonsPressed = game(groundInPinNum, groundInPin, leds, buttons, workingPins, workingPinsNum, timerScreens)
    topPercentage, place, highest, total, avg, playerCount = otherPlayerComparison(buttonsPressed)
    if gameFinished(buttonsPressed, *youScoredScreen):
        if showTopPercentage(topPercentage, *showPercentageScreen):
            showPlace(place, *placeScreen)