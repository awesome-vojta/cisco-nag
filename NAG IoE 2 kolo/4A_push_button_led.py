import RPi.GPIO as GPIO
import time

PIN_LED = 7
PIN_BUTTON = 11
BLINK_TIME = 5


GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		input_state = GPIO.input(PIN_BUTTON)
		if input_state == True:
			GPIO.output(PIN_LED, True)
			time.sleep(BLINK_TIME)
			GPIO.output(PIN_LED, False)

finally:
	GPIO.output(PIN_LED, False)
	GPIO.cleanup()
