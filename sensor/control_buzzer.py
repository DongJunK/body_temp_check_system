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
        scale = GPIO.PWM(self.BUZZER, 523)
        scale.start(10)
        sleep(0.5)
        scale.stop()

    def __del__(self):
        GPIO.cleanup()

