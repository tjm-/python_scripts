
#!/usr/bin/env python

import time
import RPi.GPIO as GPIO


# handle the button event
def buttonEventHandler (pin):
    global button_push
    print ("handling button event ", pin)
    button_push += 1
    while not GPIO.input(pin):
	    print ("False", button_push)
	    time.sleep(.5)
    # turn the green LED on
    GPIO.output(25,True)

    time.sleep(1)

    # turn the green LED off
    GPIO.output(25,False)



# main function
def main():
    global button_push
    # tell the GPIO module that we want to use 
    # the chip's pin numbering scheme
    GPIO.setmode(GPIO.BCM)

    # setup pin 23 as an input
    # and set up pins 24 and 25 as outputs
    GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(24,GPIO.OUT)
    GPIO.setup(25,GPIO.OUT)

    # tell the GPIO library to look out for an 
    # event on pin 23 and deal with it by calling 
    # the buttonEventHandler function
    GPIO.add_event_detect(23,GPIO.FALLING, bouncetime=200)
    GPIO.add_event_callback(23,buttonEventHandler)

    # turn off both LEDs
    GPIO.output(25,False)
    GPIO.output(24,True)
    # make the red LED flash
    while True:
        GPIO.output(24,True)
        time.sleep(1)
        GPIO.output(24,False)
        time.sleep(1)
        print ("main ", button_push)
        if button_push > 7:
            button_push = 0
    GPIO.cleanup()



if __name__=="__main__":
    try:
        button_push=2
        main()
    finally:
        GPIO.cleanup()
        print("Closed Everything. END")
#End



