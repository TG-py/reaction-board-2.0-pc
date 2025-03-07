from setup import setup
from loading import loading
from pre_render import preRender
from game_setup import gameSetup
from game_start import gameStart
from game import game
from game_finished import gameFinished
from between_games import betweenGames
from other_player_comparison import otherPlayerComparison
from show_top_percentage import showTopPercentage
from show_place import showPlace


#sound on button press to stop confusion on multiple presses of the same button
#lights show on buttons when not being played to draw people in


screen, winX, winY, highest, total, avg, playerCount, gameTime, realBoard = setup()
loading(screen)
groundInPinNum, groundInPin, leds, buttons, workingPins, workingPinsNum = gameSetup()
gameScreen, timerScreens, youScoredScreen, betweenGamesScreen, showPercentageScreen, placeScreen = preRender(gameTime, screen, winX, winY)
while True:
    betweenGames(highest, total, avg, playerCount, *betweenGamesScreen, screen, winX, winY)
    gameStart(gameScreen, screen)
    buttonsPressed = game(groundInPinNum, groundInPin, leds, buttons, workingPins, workingPinsNum, timerScreens, gameTime, realBoard, screen)
    topPercentage, place, highest, total, avg, playerCount = otherPlayerComparison(buttonsPressed)
    if gameFinished(buttonsPressed, *youScoredScreen, screen, winX, winY):
        if showTopPercentage(topPercentage, *showPercentageScreen, screen, winX, winY):
            showPlace(place, *placeScreen, screen, winX, winY)