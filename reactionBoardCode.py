from gpiozero import Button, LED
import random
import time


def updateTimer(startTime):
    newTime = startTime-time.time()
    #print(newTime)
    return newTime

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
        
    
    return groundInPinNum, groundInPin, ledNums, leds, buttonNums, buttons, workingPins
        
def game(groundInPinNum, groundInPin, ledNums, leds, buttonNums, buttons, workingPins):
    
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
            if 0 > updateTimer(startTime):
                breakVar = True
                break
        if breakVar: break
        leds[buttonNum].off()
        while buttons[buttonNum].is_pressed:
            if 0 > updateTimer(startTime):
                breakVar = True
                break
        if breakVar: break
    timer = updateTimer(startTime)
    for i in leds:
        i.off()

groundInPinNum, groundInPin, ledNums, leds, buttonNums, buttons, workingPins = gameSetup()
game(groundInPinNum, groundInPin, ledNums, leds, buttonNums, buttons, workingPins)