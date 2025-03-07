import pygame
import time

def gameFinished(buttonsPressed, youScoredScreen, scoreFont, continueButton, screen, winX, winY):
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