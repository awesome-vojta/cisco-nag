# coding=utf-8
import Adafruit_BMP.BMP085 as BMP085 #knihovna barometru

import urllib2	
#import bh1750
import RPi.GPIO as GPIO		
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.IN)		     #PIR cidlo

import Adafruit_DHT as dht	     #knihovna DHT22
import lcddriver		     #knihovna displeje

from time import *
import socket
import fcntl
import struct
import sys
import smbus

def init():
	global lcd
	lcd = lcddriver.lcd()
	global sensor
	sensor = BMP085.BMP085()    	
	global lcdPrint
	lcdPrint = lcd.lcd_display_string

sleep(0.1)
def print_lcd(first_line, second_line):			#definuje radky
	lcd.lcd_display_string(str(first_line), 1)	#displeje
    	lcd.lcd_display_string(str(second_line), 2)


def read_dht(gpio_pin):					#kouka jestli dht
	return (dht.read_retry(dht.DHT22, gpio_pin))	#komunikuje

def send_dht(temperature, humidity):			#odesila data z dht
	urllib2.urlopen("https://ioe.zcu.cz/th.php?id="	#na soutezni web
		"ID týmu trablšùtink"
		"&temperature={0:.1f}"
		"&humidity={1:.1f}".format(temperature,humidity))

def read_temp_raw(dallas_file):				#hleda soubor ze
	f = open(dallas_file, 'r')			#ktereho se cte
	lines = f.readlines()				#teplota na DS18B20
	f.close()
	return lines
def read_temp(dallas_file):
	lines = read_temp_raw(dallas_file)
	while lines[0].strip()[-3:] != 'YES':
		sleep(0.2)
		lines = read_temp_raw(dallas_file)
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		return temp_c
def read_dallas(id):
	base_dir = '/sys/bus/w1/devices/'
	device_folder = base_dir + id
	device_file = device_folder + '/w1_slave'	#cte teplotu z DS18B20
	return read_temp(device_file)

	
init()
while True:
	humidity,temperature = read_dht(4)
	#read_dallas("28-0000072a3590")
	sleep(0.5)
	if GPIO.input(26) == 1:
		lcdPrint("Venku je", 1)
		sleep(1.5)
		lcdPrint(("  {0:.1f} C").format(float(temperature)), 1)
		sleep(3)
		lcdPrint(("Vlhkost: {0:.1f} %").format(float(humidity)), 1)
		sleep(3)
		lcdPrint("Tlak:{0:.0f}Pa".format(sensor.read_pressure()), 1)
		sleep(3)
		lcdPrint("N. Vyska:{0:.1f}m".format(sensor.read_altitude()), 1)
		send_dht(temperature, humidity)
		sleep(3)
		lcdPrint("Pokojova teplota", 1)
#		sleep(2)
		lcdPrint("  {0:.2f} C".format(read_dallas("28-0000072a3590")), 1)
		sleep(3)
		lcd.lcd_clear()
	else:
		lcd.lcd_clear()

#	print(read_dallas("28-00000728d864"))
#	print(read_dallas("28-00000728d543"))
#	sleep(5)
