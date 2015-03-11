import unittest

from kao_io.file_line import FileLine
from metadata.python.function_start_detector import FunctionStartDetector

class isStart(unittest.TestCase):
    """ Test cases of isStart """
    FUNC_START = FileLine(0, ["def "])
    FUNC_START_WHITESPACE = FileLine(0, ["\tdef "])
    NOT_FUNC_START = FileLine(0, [""])
    
    def setUp(self):
        """ Build the detector for the test """
        self.detector = FunctionStartDetector()
        
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

# Collect all test cases in this file
suites = [suiteIsStart]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)