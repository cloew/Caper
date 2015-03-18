from kao_file import SectionFinder

class FunctionFinder:
    """ Represents a method of finding a function from the body of a file """
    
    def __init__(self, detector):
        """ Initialize the Fn Finder with the detector to use for finding the functions start and end """
        self.sectionFinder = SectionFinder(detector)
        
    def find(self, file, lineNumber):
        """ Returns the section for the function that encapsulate the given line number or None """
        section = self.sectionFinder.find(file, startAt=lineNumber, direction=SectionFinder.UP)
        if section is not None and not self.requestedLineInSection(lineNumber, section):
            return None
            
        return section
        
    def requestedLineInSection(self, currentLine, section):
        """ Return if the current line is actually within the section """
        return section.startIndex <= currentLine <= section.endIndex