from micropyserver import MicroPyServer
import json
from user import RequestHandling
from site import  html

parameters = {
    "identification_auto":"on",
    "code":"3340",
    "regime":"on",
    "on_time":"",
    "work_period":"",
    "brightness":"50",
    "manual":"on",
    "demo":"",
    }
def page_main(request):
    if request.find("GET / HTTP/1.1") == -1:
        rh = RequestHandling()
        arguments = rh.get_arguments(request)
        print(arguments)
        parameters.update(arguments)
        print(parameters)
    print(request)
    responce = html
    server.send(responce)


server = MicroPyServer() 
server.add_route("/", page_main)
server.add_route("/params", page_main)


server.start()
