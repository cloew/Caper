from kao_decorators import proxy_for

@proxy_for('lines', ['__len__', '__iter__', '__getitem__'])
class FileSection:
    """ Represents a section of a file """
    
    def __init__(self, startingLine, endingLine, lines):
        """ Initialize the file section with the lines it encompasses """
        self.startIndex = startingLine.lineIndex
        self.endIndex = endingLine.lineIndex
        self.lines = lines[self.startIndex: self.endIndex+1]