from machine import Pin, freq, PWM

import uasyncio
from time import sleep
from gc import collect
from user import WifiConnection
collect()

ssid = 'garlic'
password = 'uzol1354'

ap_parameters = {
    "ssid": "PWA",
    "password": "12345678"
    }

st_parameters = {
    "ssid": "garlic",
    "password": "uzol1354"
    }

wifi = WifiConnection(ap_parameters)

wifi.make_access_point()
# wifi.connect_to_station()


# #LED = Pin(15, Pin.OUT)
# 
# async def blink(period_ms, times):
#     global counter_led
#     while counter_led<times:
#         LED.value(not LED.value())
#         counter_led += 1
#         await uasyncio.sleep_ms(period_ms)
#     LED.off()
# uasyncio.run(blink(1000, 3))

