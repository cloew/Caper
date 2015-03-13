import json

class PrintHandler:
    """ Output Handler that simply prints the received data """
    
    def output(self, data):
        """ Output the data by simply printing it """
        print(json.dumps(data))