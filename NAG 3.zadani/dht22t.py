# coding=utf-8

import Adafruit_DHT as dht
h,t = dht.read_retry(dht.DHT22, 4)
print 'Teplota={0:0.1f}°C  Vlhkost={1:0.1f}%'.format(t, h)
