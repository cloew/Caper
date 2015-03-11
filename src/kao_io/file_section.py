from kao_decorators import proxy_for

@proxy_for('lines', ['__len__', '__iter__', '__getitem__'])
class FileSection:
    """ Represents a section of a file """
    
    def __init__(self, startingLineNumber, endingLineNumber, lines):
        """ Initialize the file section with the lines it encompasses """
        self.startIndex = startingLineNumber
        self.endIndex = endingLineNumber
        self.lines = lines[self.startIndex: self.endIndex+1]
        
    def __eq__(self, other):
        """ Return if this section equals the other section """
        return self.startIndex == other.startIndex and self.endIndex == other.endIndex and self.lines == other.lines