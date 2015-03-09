
def DummyDetector(index):
    """ Represents a function start or end detector that returns true for the index provided """
    class Dummy:
        def __init__(self, startingLine=None):
            pass
            
        def isStart(self, line):
            return line.lineIndex == index
            
        def isEnd(self, line):
            return line.lineIndex == index
    return Dummy