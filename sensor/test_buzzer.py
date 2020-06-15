import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
buzz = 16

GPIO.setwarnings(False)
GPIO.setup(buzz, GPIO.OUT)
freq = [523,587,659,698,784,880,988,1047]

def makeTone(freq):
	scale = GPIO.PWM(buzz, freq)
	scale.start(10)
	sleep(0.5)
	scale.stop()

try:
	while(True):
		makeTone(523)
		sleep(20)
except KeyboardInterrupt:
	GPIO.cleanup()
