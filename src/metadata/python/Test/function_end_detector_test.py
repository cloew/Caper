import unittest

from kao_file.file_line import FileLine
from metadata.python.function_end_detector import FunctionEndDetector

class isEnd(unittest.TestCase):
    """ Test cases of isEnd """
    IN_FN_BODY = FileLine(1, ["def ", "\tpass", "\tpass"])
    END_OF_FILE = FileLine(2, ["def ", "\tpass", "\tpass"])
    END_OF_FN = FileLine(2, ["def ", "\tpass", "\tpass", ""])
    
    def withinFunction(self):
        """ Test that isEnd returns properly when within the function body still """
        detector = FunctionEndDetector(self.IN_FN_BODY.lines[0])
        self.assertFalse(detector.isEnd(self.IN_FN_BODY))
        
    def atEndOfFile(self):
        """ Test that isEnd returns properly when at the end of the file """
        detector = FunctionEndDetector(self.END_OF_FILE.lines[0])
        self.assertTrue(detector.isEnd(self.END_OF_FILE))
        
    def atEndOfFunction(self):
        """ Test that isEnd returns properly when at the end of the function """
        detector = FunctionEndDetector(self.END_OF_FN.lines[0])
        self.assertTrue(detector.isEnd(self.END_OF_FN))

# Collect all test cases in this class
testcasesIsEnd = ["withinFunction", "atEndOfFile", "atEndOfFunction"]
suiteIsEnd = unittest.TestSuite(map(isEnd, testcasesIsEnd))

##########################################################

# Collect all test cases in this file
suites = [suiteIsEnd]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)