import unittest

from kao_file.kao_file import KaoFile
from kao_file.file_section import FileSection
from metadata.general.function_finder import FunctionFinder
from Test.dummy_detector import DummyDetector

class find(unittest.TestCase):
    """ Test cases of find """
    
    def buildFinder(self, fnStartsOn=0, fnEndsOn=0):
        return FunctionFinder(DummyDetector(fnStartsOn), DummyDetector(fnEndsOn))
        
    def withinFunction(self):
        """ Test that when the requested line is within the function finder returns properly """
        fnStart = 0
        fnEnd = 2
        lines = ["Line 1", "Line 2", "Line 3", "Line 4"]
        expected = FileSection(fnStart, fnEnd, lines)
        
        finder = self.buildFinder(fnStartsOn=fnStart, fnEndsOn=fnEnd)
        functionLines = finder.find(1, KaoFile(lines))
        self.assertEqual(expected, functionLines)
        
    def noLines(self):
        """ Test that when there are no lines the function finder returns properly """
        finder = self.buildFinder(fnStartsOn=0, fnEndsOn=1)
        functionLines = finder.find(0, KaoFile([]))
        self.assertIsNone(functionLines)
        
    def noFunctionStart(self):
        """ Test that when there is no function start the finder returns properly """
        finder = self.buildFinder(fnStartsOn=-1, fnEndsOn=1)
        functionLines = finder.find(2, KaoFile(["", "", ""]))
        self.assertIsNone(functionLines)
        
    def afterFunctionEnd(self):
        """ Test that when the requested line is after the function the finder returns properly """
        finder = self.buildFinder(fnStartsOn=0, fnEndsOn=1)
        functionLines = finder.find(2, KaoFile(["", "", ""]))
        self.assertIsNone(functionLines)

# Collect all test cases in this class
testcasesFind = ["withinFunction", "noLines", "noFunctionStart", "afterFunctionEnd"]
suiteFind = unittest.TestSuite(map(find, testcasesFind))

##########################################################

# Collect all test cases in this file
suites = [suiteFind]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)