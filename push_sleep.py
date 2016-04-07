
#!/usr/bin/env python

import time
import threading
import RPi.GPIO as GPIO



# handle the button event
def buttonEventHandler (pin):
    global button_push, ev
    button_push = not GPIO.input(pin)
    print ('int ', button_push)
    ev.set()


# main function
def main():
    global button_push, ev
    duration=[1, .5, 2]
    sleep_interval=[.5, 2, 1]

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
    GPIO.add_event_detect(23,GPIO.BOTH, bouncetime=10)
    GPIO.add_event_callback(23,buttonEventHandler)

    # turn on RED and Green off
    GPIO.output(25,False)
    GPIO.output(24,True)
    #
    while True:
        ev.clear()
        ev.wait(timeout=1)
        print ("main ", button_push)
        while button_push:
            for i in range(len(duration)):
                print(i)
                GPIO.output(25, True)
                ev.clear()
                ev.wait(timeout=duration[i])
                print ('pus", button_push)
                GPIO.output(25, False)
                if ev.is_set():
                    break
                ev.wait(timeout=sleep_interval[i])
    GPIO.cleanup()



if __name__=="__main__":
    try:
        button_push=False
        ev=threading.Event()
        main()
    finally:
        GPIO.cleanup()
        print("Closed Everything. END")
#End



