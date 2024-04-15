from micropyserver import MicroPyServer

from user import RequestHandling, json_load, json_save
from site import html, css


def page_main(request):
    if request.find("GET / HTTP/1.1") == -1:
        rh = RequestHandling(["identification_auto",
                              "regime",
                              "manual",
                              "demo"])
        arguments = rh.get_arguments(request)	# get GET arguments from request
        p = json_load('parameters.json')	# get parameters dict from file
        p.update(arguments)	# update parameters dict with new arguments from request
        p = rh.correct_arguments(p, arguments)	# correction of arguments (для того чтобы инвертировать чекбоксы)
        json_save('parameters.json', p)	# save parameters into file
    print(request)
    p = json_load('parameters.json')	# get parameters
    print(type(p))
    print(p)
    responce = html % (css,
                       p["identification_auto"],
                       p["code"],
                       p["regime"],
                       p["on_time"],
                       p["work_period"],
                       p["brightness"],
                       p["manual"],
                       p["demo"])	# format responce
    server.send(responce)

    
server = MicroPyServer() 
server.add_route("/", page_main)


server.start()
