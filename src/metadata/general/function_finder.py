from kao_io.file_line import FileLine

class FunctionFinder:
    """ Represents a method of finding a function from the body of a file """
    
    def __init__(self, startDetectorCls, endDetectorCls):
        """ Initialize the Fn Finder with the detectors to use for finding the functions start and end """
        self.startDetectorCls = startDetectorCls
        self.endDetectorCls = endDetectorCls
        
    def find(self, lineNumber, lines):
        """ Returns the function lines that encapsulate the given line number or None """
        if len(lines) == 0:
            return None
            
        currentLine = FileLine(lineNumber, lines)
        startingLine = self.findStartingLine(currentLine)
        if startingLine is None:
            return None
            
        endingLine = self.findEndingLine(startingLine)
        if endingLine is None:
            return endingLine
            
        if not self.requestedLineWithinFunction(currentLine, startingLine, endingLine):
            return None

        return lines[startingLine.lineIndex: endingLine.lineIndex+1]
            
    def findStartingLine(self, currentLine):
        """ Returns the strating line of the function or None """
        startingLine = currentLine
        startDetector = self.startDetectorCls()
        while not startDetector.isStart(startingLine) and not startingLine.isFirstLine():
            startingLine = startingLine.previous()
        
        return startingLine if startDetector.isStart(startingLine) else None
            
    def findEndingLine(self, startingLine):
        """ Returns the strating line of the function or None """
        if startingLine.isLastLine():
            return None
        
        endingLine = startingLine.next()
        endDetector = self.endDetectorCls(startingLine)
        while not endDetector.isEnd(endingLine) and not endingLine.isLastLine():
            endingLine = endingLine.next()
        
        return endingLine if endDetector.isEnd(endingLine) else None
        
    def requestedLineWithinFunction(self, currentLine, startingLine, endingLine):
        """ Return if the current line is actually within the function """
        return startingLine.lineIndex <= currentLine.lineIndex <= endingLine.lineIndex