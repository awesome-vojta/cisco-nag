import RPi.GPIO as GPIO
import time
import urllib2

response = urllib2.urlopen("https://ioe.zcu.cz/morse.php?id=fdnGYpKcZdeovvGpxCzAUo20LlSgQQSA")
html = response.read()

PIN_LED_RED = 4
PIN_LED_GREEN = 24
PIN_LED_BLUE = 18


DOT_TIME = 1
DASH_TIME = 2
SLASH_TIME = 2
SPACE_TIME = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED_RED, GPIO.OUT)
GPIO.setup(PIN_LED_GREEN, GPIO.OUT)
GPIO.setup(PIN_LED_BLUE, GPIO.OUT)

GPIO.output(PIN_LED_BLUE, True)
GPIO.output(PIN_LED_GREEN, True)

try:
	for c in html:
		if c == ".":
			time.sleep(DOT_TIME)
			GPIO.output(PIN_LED_RED, False)
			time.sleep(DOT_TIME)
			GPIO.output(PIN_LED_RED, True)
		if c == "-":
			time.sleep(DOT_TIME)
			GPIO.output(PIN_LED_RED, False)
			time.sleep(DASH_TIME)
			GPIO.output(PIN_LED_RED, True)
		if c == "/":
			time.sleep(SLASH_TIME)
		if c == " ":
			time.sleep(SPACE_TIME)
			
		
finally:

	GPIO.cleanup()
