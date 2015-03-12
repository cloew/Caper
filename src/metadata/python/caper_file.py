from kao_io.kao_file import KaoFile

from metadata.general.function_finder import FunctionFinder
from metadata.python.function_end_detector import FunctionEndDetector
from metadata.python.function_start_detector import FunctionStartDetector
from metadata.python.caper_function import CaperFunction
from metadata.python.python_function import PythonFunction
from metadata.python.caper_function_caller import CaperFunctionCaller

class CaperFile:
    """ Represents a file that can be used by Caper to extract the context of a function """
    
    def __init__(self, filename, lineNumber, destination=None):
        """ Initialize the Caper Runner with the file to run and the location within it to run """
        self.file = KaoFile(filename)
        self.lineNumber = lineNumber-1
        
        if destination is None:
            destination = 'temp.py.caper'
        self.destination = destination
        
    def create(self):
        """ Create the Caper File """
        caperFn = self.replaceFunctionWithCaperFunction()
        caller = CaperFunctionCaller(caperFn)
        self.file.append(caller.lines)
        self.file.save(self.destination)
        
    def replaceFunctionWithCaperFunction(self):
        """ Replace the current function with a Caper Function """
        finder = FunctionFinder(FunctionStartDetector, FunctionEndDetector)
        fnSection = finder.find(self.lineNumber, self.file)
        fn = PythonFunction(fnSection)
        caperFn = CaperFunction(fn)
        self.file.replaceSection(fnSection, caperFn.lines)
        return caperFn