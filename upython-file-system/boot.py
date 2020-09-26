# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

def do_connect(ssid, pwd):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, pwd)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

# get wifi info - 
# you can create this file over serial or load it through webrepl
import wifi_config

# Attempt to connect to WiFi network
do_connect(wifi_config.ssid, wifi_config.password)

import webrepl
webrepl.start()
