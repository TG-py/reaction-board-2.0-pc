import pygame
import time

def showPlace(place, placeScreen, placeFont, continueButton, screen, winX, winY):
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