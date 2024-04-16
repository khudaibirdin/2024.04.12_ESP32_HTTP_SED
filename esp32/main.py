import machine
import time

from micropyserver import MicroPyServer
from user import RequestHandling, json_load, json_save
from site import html, css
import _thread


def page_main(request):
    """
    Обработка главной страницы
    """
    if request.find("GET / HTTP/1.1") == -1:	# при получении get-запроса
        rh = RequestHandling(["identification_auto",
                              "regime",
                              "manual",
                              "demo"])
        arguments = rh.get_arguments(request)	# get GET arguments from request
        p = json_load('parameters.json')	# get parameters dict from file
        p.update(arguments)	# update parameters dict with new arguments from request
        p = rh.correct_arguments(p, arguments)	# correction of arguments (для того чтобы инвертировать чекбоксы)
        p = rh.make_checked_radiobutton(p)
        json_save('parameters.json', p)	# save parameters into file
    print(request)
    p = json_load('parameters.json')	# get parameters
    print(p)
    responce = html % (css,
                       p["identification_auto"],
                       p["code"],
                       p["regime"],
                       p["on_time"],
                       p["work_period"],
                       p["brightness"],
                       p["manual"],
                       p["demo1"],
                       p["demo2"],
                       p["demo3"],
                       p["demo4"],
                       p["demo5"],
                       p["demo"])
    serv.send(responce)


def main(led, period_ms):
    """
    Поток для основных задач, логики приложения
    """
    while True:
        led.on()
        time.sleep_ms(5)
        led.off()
        time.sleep_ms(period_ms)


def server():
    """
    Поток для работы сервера, для взаимодействия ч-з браузер
    """
    serv.start()


led = machine.Pin(12, Pin.OUT)
serv = MicroPyServer()
serv.add_route("/", page_main)

try:
    _thread.start_new_thread(main, (led, 500))
    server()
except:
    machine.reset()
