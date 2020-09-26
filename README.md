# midi-pedal
esp32 upython BT midi pedal project

## First Time Setup
- Inside the project dir run `pipenv install` (this should load all the dependent python libs)
- Connect to your ESP32 board with USB/serial
- Erase flash `esptool.py --port /dev/ttyUSB0 erase_flash`
- Load a micropython bin for ESP32 `esptool.py --port /dev/tty.usb-xxx --baud 115200 write_flash --flash_size=detect 0 esp8266-20170108-v1.8.7.bin`
- connect to micropython repl via serial (MAC command) `screen /dev/tty.usb-xxx 115200`
- connect your ESP32 to your wifi
 `sta_if = network.WLAN(network.STA_IF)`
 `sta_if.active(True)`
 `sta_if.connect(ssid, pwd)`
- enable webrepl on boot `import webrepl_setup`
- start webrepl for this session (you may need to reboot for the password you set to be in effect)
 `import webrepl`
 `webrepl.start()`
- **NOTE** the ip address that webrepl is using
-  You should be able to connect to your device on the webrepl website now http://micropython.org/webrepl/#192.168.1.138:8266/
- from webrepl load the boot.py file
- create a wifi_config.py file that looks like below and load it via webrepl
```
 ssid = "my_ssid"
 password = "my_password"
```
- power cycle your device and verify you can connect over webrepl automatically now
