class RequestHandling:
    def __init__(self, args_to_correct):
        self.args_to_correct = args_to_correct
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
    
    
    def correct_arguments(self, global_dict, new_arguments):
        for i in self.args_to_correct:
            if i not in new_arguments:
                global_dict[i] = ""
        return global_dict
        


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