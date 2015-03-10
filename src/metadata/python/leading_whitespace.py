from kao_decorators import operators_via_fn

@operators_via_fn(lambda obj: len(obj))
class LeadingWhitespace:
    """ Represents the leading whitespace for a line in a Python file """
    
    def __init__(self, line):
        """ Initialize with the line to act as """
        self.whitespace = line[:len(line)-len(line.lstrip())].replace('\n', '')
        
    def __len__(self):
        """ Return the length of the leading whitespace """
        return len(self.whitespace)
        
    def __add__(self, other):
        """ Add this whitespace to a given string """
        return self.whitespace + other
        
    def __repr__(self):
        """ Return the string representation of the leading whitespace """
        return self.whitespace