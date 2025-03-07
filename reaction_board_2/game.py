import time
import random
from gpiozero import LED, Button

from real_board_switch import realBoardSwitch
from update_timer import updateTimer

def game(groundInPinNum, groundInPin, leds, buttons, workingPins, workingPinsNum, timerScreens, gameTime, realBoard):
    
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
        while not realBoardSwitch(buttons[buttonNum].is_pressed, realBoard):
            if 0 > updateTimer(startTime, timerScreens):
                breakVar = True
                break
        if breakVar: break
        buttonsPressed += 1
        leds[buttonNum].off()
        while realBoardSwitch(buttons[buttonNum].is_pressed, realBoard):
            if 0 > updateTimer(startTime, timerScreens):
                breakVar = True
                break
        if breakVar: break
    timer = updateTimer(startTime, timerScreens)
    for i in leds:
        i.off()
    return buttonsPressed