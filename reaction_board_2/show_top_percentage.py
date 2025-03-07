import pygame
import time

def showTopPercentage(percentageBeaten, showTopPercentageScreen, percentageFont, continueButton, screen, winX, winY):
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