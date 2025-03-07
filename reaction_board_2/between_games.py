import pygame

def betweenGames(highest, total, avg, playerCount, betweenGamesScreen, infoFont, startButton, screen, winX, winY):
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