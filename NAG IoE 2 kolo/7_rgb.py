import RPi.GPIO as GPIO
import time

PIN_LED_RED = 4
PIN_LED_GREEN = 24
PIN_LED_BLUE = 18

PIN_BLUE_UP = 26
PIN_BLUE_DOWN = 13
PIN_RED_UP = 16
PIN_RED_DOWN = 12
PIN_GREEN_UP = 22
PIN_GREEN_DOWN = 23

DEBOUNCE_TIME = 0.1
PWM_TIME = 100

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED_RED, GPIO.OUT)
GPIO.setup(PIN_LED_GREEN, GPIO.OUT)
GPIO.setup(PIN_LED_BLUE, GPIO.OUT)

GPIO.setup(PIN_BLUE_UP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_BLUE_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_RED_UP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_RED_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_GREEN_UP, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIN_GREEN_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

blue_intense = 0
red_intense = 0
green_intense = 0
red_pwm = GPIO.PWM(PIN_LED_RED, PWM_TIME)
green_pwm = GPIO.PWM(PIN_LED_GREEN, PWM_TIME)
blue_pwm = GPIO.PWM(PIN_LED_BLUE, PWM_TIME)

red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

#red_pwm.ChangeDutyCycle(100)
#green_pwm.ChangeDutyCycle(100)
#blue_pwm.ChangeDutyCycle(100)
try:
	while True:
		input_state = GPIO.input(PIN_BLUE_UP)
		if input_state == True:
			if blue_intense < 100:
				blue_intense = blue_intense + 1
			blue_pwm.ChangeDutyCycle(blue_intense)
			time.sleep(DEBOUNCE_TIME)
		
		input_state = GPIO.input(PIN_BLUE_DOWN)
		if input_state == True:
			if blue_intense > 0:
				blue_intense = blue_intense - 1
			blue_pwm.ChangeDutyCycle(blue_intense)
			time.sleep(DEBOUNCE_TIME)

		input_state = GPIO.input(PIN_RED_UP)
		if input_state == True:
			if red_intense < 100:
				red_intense = red_intense + 1
			red_pwm.ChangeDutyCycle(red_intense)
			time.sleep(DEBOUNCE_TIME)

		input_state = GPIO.input(PIN_RED_DOWN)
		if input_state == True:
			if red_intense > 0:
				red_intense = red_intense - 1
			red_pwm.ChangeDutyCycle(red_intense)
			time.sleep(DEBOUNCE_TIME)

		input_state = GPIO.input(PIN_GREEN_UP)
		if input_state == True:
			if green_intense < 100:
				green_intense = green_intense + 1
			green_pwm.ChangeDutyCycle(green_intense)
			time.sleep(DEBOUNCE_TIME)

		input_state = GPIO.input(PIN_GREEN_DOWN)
		if input_state == True:
			if green_intense > 0:
				green_intense = green_intense - 1
			green_pwm.ChangeDutyCycle(green_intense)
			time.sleep(DEBOUNCE_TIME)
finally:
	red_pwm.ChangeDutyCycle(0)
	green_pwm.ChangeDutyCycle(0)
	blue_pwm.ChangeDutyCycle(0)
	red_pwm.stop()
	green_pwm.stop()
	blue_pwm.stop()

	GPIO.cleanup()
