class RequestHandling:
    def __init__(self):
        pass
    
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

