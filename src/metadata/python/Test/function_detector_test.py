import unittest

from kao_file.file_line import FileLine
from metadata.python.function_detector import FunctionDetector

class isStart(unittest.TestCase):
    """ Test cases of isStart """
    FUNC_START = FileLine(0, ["def "])
    FUNC_START_WHITESPACE = FileLine(0, ["\tdef "])
    NOT_FUNC_START = FileLine(0, [""])
    
    def setUp(self):
        """ Build the detector for the test """
        self.detector = FunctionDetector()
        
    def noWhitespace(self):
        """ Test that a function without preceding whitespace is detected properly """
        self.assertTrue(self.detector.isStart(self.FUNC_START))
        
    def withWhitespace(self):
        """ Test that a function with preceding whitespace is detected properly """
        self.assertTrue(self.detector.isStart(self.FUNC_START_WHITESPACE))
        
    def notFunction(self):
        """ Test that a non-function line is detected properly """
        self.assertFalse(self.detector.isStart(self.NOT_FUNC_START))

# Collect all test cases in this class
testcasesIsStart = ["noWhitespace", "withWhitespace", "notFunction"]
suiteIsStart = unittest.TestSuite(map(isStart, testcasesIsStart))

##########################################################

class isEnd(unittest.TestCase):
    """ Test cases of isEnd """
    IN_FN_BODY = FileLine(1, ["def ", "\tpass", "\tpass"])
    END_OF_FILE = FileLine(2, ["def ", "\tpass", "\tpass"])
    END_OF_FN = FileLine(2, ["def ", "\tpass", "\tpass", ""])
    
    def withinFunction(self):
        """ Test that isEnd returns properly when within the function body still """
        detector = FunctionDetector(startingLine=self.IN_FN_BODY.lines[0])
        self.assertFalse(detector.isEnd(self.IN_FN_BODY))
        
    def atEndOfFile(self):
        """ Test that isEnd returns properly when at the end of the file """
        detector = FunctionDetector(startingLine=self.END_OF_FILE.lines[0])
        self.assertTrue(detector.isEnd(self.END_OF_FILE))
        
    def atEndOfFunction(self):
        """ Test that isEnd returns properly when at the end of the function """
        detector = FunctionDetector(startingLine=self.END_OF_FN.lines[0])
        self.assertTrue(detector.isEnd(self.END_OF_FN))

# Collect all test cases in this class
testcasesIsEnd = ["withinFunction", "atEndOfFile", "atEndOfFunction"]
suiteIsEnd = unittest.TestSuite(map(isEnd, testcasesIsEnd))

##########################################################

# Collect all test cases in this file
suites = [suiteIsStart, suiteIsEnd]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)