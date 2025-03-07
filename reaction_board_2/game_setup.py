from gpiozero import Button, LED

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