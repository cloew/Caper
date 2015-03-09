
class LeadingWhitespace:
    """ Represents the leading whitespace for a line in a Python file """
    
    def __init__(self, line):
        """ Initialize with the line to act as """
        self.whitespace = line[:len(line)-len(line.lstrip())]
        
    def __len__(self):
        """ Return the length of the leading whitespace """
        return len(self.whitespace)
        
    def __lt__(self, other):
        """ Return if this leading whitespace is less than the other """
        return len(self) < len(other)
        
    def __eq__(self, other):
        """ Return if this leading whitespace is equal to the other """
        return len(self) == len(other)
        
    def __le__(self, other):
        return self < other or self == other