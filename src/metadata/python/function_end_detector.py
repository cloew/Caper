from .leading_whitespace import LeadingWhitespace

class FunctionEndDetector:
    """ Detects the end of a Python function """
    
    def __init__(self, startingLine):
        """ Initialize with the identation of the start of the function """
        self.startingLine = startingLine
    
    def isEnd(self, line):
        """ Returns if the given line is the end of a Python  """
        if line.isLastLine():
            return True
        else:
            return LeadingWhitespace(line.next()) <= LeadingWhitespace(self.startingLine)