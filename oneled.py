import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
for x in range(0,10):
	GPIO.output(18, True)
	time.sleep(0.05)
	GPIO.output(18, False)
	time.sleep(0.45)
GPIO.cleanup()
