from machine import Pin, freq, PWM
import network
import uasyncio
from time import sleep
from gc import collect

collect()

ssid = 'garlic'
password = 'uzol1354'
counter = 0
#station = network.WLAN(network.STA_IF)
station = network.WLAN(network.AP_IF)
station.active(True)
counter_led = 0

#LED = Pin(15, Pin.OUT)

async def blink(period_ms, times):
    """
    Асинхронная функция моргания светодиодом по требованию
    """
    global counter_led
    while counter_led<times:
        LED.value(not LED.value())
        counter_led += 1
        await uasyncio.sleep_ms(period_ms)
    LED.off()


def connect_wifi(station):
    global counter
    sleep(1)
    #station.connect(ssid, password)
    station.active(True)
    #station.ifconfig('192.168.100.205','255.255.255.0','192.168.100.2','8.8.8.8')
    station.config(essid='PWA', authmode=network.AUTH_WPA_WPA2_PSK, password='12345678')
    counter += 1


sleep(5)
while station.isconnected() == False:
    try:
        connect_wifi(station)
    except:
        pass
    if counter == 5:
        #uasyncio.run(blink(Pin(15), 1000, 7))
        break

#uasyncio.run(blink(1000, 3))
print('Connection successful')
print(station.ifconfig())
