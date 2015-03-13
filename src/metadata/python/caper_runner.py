from .caper_file import CaperFile

import json
import subprocess

class CaperRunner:
    """ Responsible for generating and running the caper function """
    
    def __init__(self, filename, lineNumber, executable):
        """ Initialize the Caper Runner with the file to run and the location within it to run """
        self.caperFile = CaperFile(filename, lineNumber)
        self.executable = executable
        
    def run(self):
        """ Run the Caper Function """
        self.caperFile.create()
        return self.getOutput()
        
    def getOutput(self):
        """ Retrieve the output from the caper file """
        output = subprocess.check_output([self.executable, self.caperFile.destination])
        output = output.decode("utf-8")
        return json.loads(output)