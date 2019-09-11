# This file is executed on every boot (including wake-boot from deepsleep)

import esp
esp.osdebug(None)

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import gc
gc.collect()


# put your ssid and password here
ssid = 'xxxx' 
password = 'xxxx'

# set static ip
ip        = '192.168.178.20'
subnet    = '255.255.255.0'
gateway   = '192.168.1.1'
dns       = '1.1.1.1'

# set led pin to output
led = Pin(23, Pin.OUT)

# connect to wifi
station = network.WLAN(network.STA_IF)

station.active(True)
station.ifconfig((ip,subnet,gateway,dns))
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection')
print(station.ifconfig())
