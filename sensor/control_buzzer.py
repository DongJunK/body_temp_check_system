import RPi.GPIO as GPIO
from time import sleep
from sensor_config import SensorConfig

class BuzzerControl:
    BUZZER = SensorConfig.BUZZER_PIN
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.BUZZER, GPIO.OUT)

    def turn_on_buzzer(self):
        GPIO.output(self.BUZZER, GPIO.HIGH)
        sleep(0.6)
        GPIO.output(self.BUZZER, GPIO.LOW)
   

