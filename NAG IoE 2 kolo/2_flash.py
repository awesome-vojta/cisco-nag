import RPi.GPIO as GPIO
import time

PIN_LED = 18
BLINK_TIME = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)

try:
    while True:
        GPIO.output(PIN_LED, False)
        time.sleep(BLINK_TIME)
        GPIO.output(PIN_LED, True)
        time.sleep(BLINK_TIME)
finally:
    GPIO.cleanup()
