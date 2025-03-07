import pygame

def preRender(gameTime, screen, winX, winY):
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