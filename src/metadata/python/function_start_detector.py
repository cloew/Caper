
class FunctionStartDetector:
    """ Detects the start of a Python function """
    
    def isStart(self, line):
        """ Return if the given line is the start of a Python function """
        return line.lstrip().startswith("def ")