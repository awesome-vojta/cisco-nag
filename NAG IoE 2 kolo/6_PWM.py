import RPi.GPIO as GPIO
import time

PIN_LED = 7
PIN_BUTTON = 11
BLINK_TIME = 5
PWM_TIME = 1000

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

light_on = False
p = GPIO.PWM(PIN_LED, PWM_TIME) 
p.start(0)
try:
	while True:
		input_state = GPIO.input(PIN_BUTTON)
		if input_state == True:
			if light_on == False:
				for i in range(0, 101, 1):
					p.ChangeDutyCycle(i)
					print(i)
					time.sleep(0.02)
				# p.ChangeDutyCycle(100)
				light_on = True
			else:
				for i in range(100, -1, -1):
					p.ChangeDutyCycle(i) 
					print(i)
					time.sleep(0.02)
				# p.ChangeDutyCycle(0)
				light_on = False

finally:
	p.stop()
	GPIO.output(PIN_LED, False)
	GPIO.cleanup()
