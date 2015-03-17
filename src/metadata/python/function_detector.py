from .leading_whitespace import LeadingWhitespace

class FunctionDetector:
    """ Detects a Python function """
    
    def __init__(self, startingLine=None):
        """ Initialize the function detector """
        self.startingLine = startingLine
    
    def isStart(self, line):
        """ Return if the given line is the start of a Python function """
        isStart = line.lstrip().startswith("def ")
        if isStart:
            self.startingLine = line
        return isStart
        
    def isEnd(self, line):
        """ Returns if the given line is the end of a Python Function """
        if line.isLastLine():
            return True
        else:
            return LeadingWhitespace(line.next()) <= LeadingWhitespace(self.startingLine)