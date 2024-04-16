import time
import network


class RequestHandling:
    def __init__(self, args_to_correct):
        self.args_to_correct = args_to_correct
    
    
    def get_arguments(self, request):
        """
        GET /get?input_FREQUENCY=100&input_DUTY=200&input_DIRECTION=300 HTTP/1.1
        """
        arguments = {}
        data_string = request[request.find("/?")+len("/?"):request.find(" HTTP/1.1")]+"&"
        while True:
            variable = data_string[:data_string.find("=")]
            data_string = data_string[data_string.find("=")+len("="):]
            value = data_string[:data_string.find("&")]
            data_string = data_string[data_string.find("&")+len("&"):]
            arguments[variable] = value
            if data_string.find("=") == -1:
                break
        return arguments
    
    
    def correct_arguments(self, global_dict, new_arguments):
        for i in self.args_to_correct:
            if i not in new_arguments:
                global_dict[i] = ""
        return global_dict
    
    
    def make_checked_radiobutton(self, params):
        
        
        if params["demo_type"] == "1":
            params["demo1"] = "checked"
            params["demo2"] = params["demo3"] = params["demo4"] = params["demo5"] = ""
        if params["demo_type"] == "2":
            params["demo2"] = "checked"
            params["demo1"] = params["demo3"] = params["demo4"] = params["demo5"] = ""
        if params["demo_type"] == "3":
            params["demo3"] = "checked"
            params["demo1"] = params["demo2"] = params["demo4"] = params["demo5"] = ""
        if params["demo_type"] == "4":
            params["demo4"] = "checked"
            params["demo1"] = params["demo2"] = params["demo3"] = params["demo5"] = ""
        if params["demo_type"] == "5":
            params["demo5"] = "checked"
            params["demo1"] = params["demo2"] = params["demo3"] = params["demo4"] = ""
        return params


def json_load(path):
    import json
    try:
        with open(path, 'r') as f:
            p = json.load(f)
            return p
    except:
            print("Error! Could not save")


def json_save(path, obj):
    import json
    try:
        with open('parameters.json', 'w') as f:
            json.dump(obj, f)
    except:
            print("Error! Could not save")
           
           
class WifiConnection:
    """
    Подключение к сети, создание точки доступа, контроль подключения
    """
    
    def __init__(self, settings):
        self.settings = settings
        self.error_counter = 0
    
    
    def make_access_point(self):
        access_point = network.WLAN(network.AP_IF)
        access_point.active(True)
        access_point.config(essid=self.settings["ssid"],
                       authmode=network.AUTH_WPA_WPA2_PSK,
                       password=self.settings["password"])
        time.sleep(5)
        if access_point.active():
            print("Access point is activated")
            print(access_point.ifconfig())
        else:
            print("Access point error")
        
    
    def connect_to_station(self):
        station = network.WLAN(network.STA_IF)
        station.active(True)
        self.__try_to_connect(station)
        self.error_counter = 0
        if station.isconnected():
            print("Successfull connection")
            print(station.ifconfig())
        else:
            print("Connection error")
        
    
    def __try_to_connect(self, station):
        while station.isconnected() == False:
            try:
                station.connect(self.settings["ssid"], self.settings["password"])
            except:
                self.error_counter += 1
                time.sleep(1)
                if self.error_counter == 5:
                    break
        

    
        
        
        