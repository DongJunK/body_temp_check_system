import RPi.GPIO as GPIO
from sensor_config import SensorConfig

class LedControl:
    GREEN_LED = SensorConfig.GREEN_LED_PIN
    RED_LED = SensorConfig.RED_LED_PIN
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.GREEN_LED, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.RED_LED, GPIO.OUT, initial=GPIO.LOW)
    
    def turn_on_green(self):
        GPIO.output(self.GREEN_LED, GPIO.HIGH)
    
    def turn_on_red(self):
        GPIO.output(self.RED_LED, GPIO.HIGH)
    
    def turn_off_green(self):
        GPIO.output(self.GREEN_LED, GPIO.LOW)

    def turn_off_red(self):
        GPIO.output(self.RED_LED, GPIO.LOW)

    def __del__(self):
        GPIO.cleanup()
