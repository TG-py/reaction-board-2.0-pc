import pygame
import pickle

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