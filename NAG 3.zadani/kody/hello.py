import lcddriver
from time import *

import socket
import fcntl
import struct

#def get_ip_address(ifname):
#    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    return socket.inet_ntoa(fcntl.ioctl(
#        s.fileno(),
#        0x8915,  # SIOCGIFADDR
#        struct.pack('256s', ifname[:15])
#    )[20:24])
#
#def get_first_ip():
#    for s in ['wlan0','eth0']:
#        try:
#            ip = get_ip_address(s)
#            return ip
#        except IOError:
#            pass
#    return 'not connected'

#get_ip_address('eth0')  # '192.168.0.110'


lcd = lcddriver.lcd()
start = time()
seconds_connected = 0
while True:
    lcd.lcd_display_string("Trablsutynk", 1)
    lcd.lcd_display_string("       (.Y.)", 2)
    sleep(0.1)
