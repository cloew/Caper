from kao_io.file_line import FileLine
from kao_io.file_section import FileSection

from kao_decorators import proxy_for

@proxy_for('lines', ['__len__'])
class KaoFile:
    """ Represents a file """
    
    def __init__(self, filename=None, lines=None):
        """ Initialize the file """
        if filename is not None:
            with open(filename, 'r') as file:
                self.lines = file.readlines()
        elif lines is not None:
            self.lines = lines
        else:
            raise TypeError("Either Filename or lines must be provided")
            
    def getLineAt(self, index):
        """ Return the File Line at the given index """
        return FileLine(index, self.lines)
            
    def getSection(self, startingLine, endingLine):
        """ Return the File Section for the given lines """
        return FileSection(startingLine.lineIndex, endingLine.lineIndex, self.lines)