import unittest

from metadata.general.file_line import FileLine

class isFirstLine(unittest.TestCase):
    """ Test cases of isFirstLine """
        
    def isFirst(self):
        """ Test that when it is the first line it returns properly """
        line = FileLine(0, ["", "", ""])
        self.assertTrue(line.isFirstLine())
        
    def isMiddle(self):
        """ Test that when it is the middle line it returns properly """
        line = FileLine(1, ["", "", ""])
        self.assertFalse(line.isFirstLine())
        
    def isLast(self):
        """ Test that when it is the last line it returns properly """
        line = FileLine(2, ["", "", ""])
        self.assertFalse(line.isFirstLine())

# Collect all test cases in this class
testcasesIsFirstLine = ["isFirst", "isMiddle", "isLast"]
suiteIsFirstLine = unittest.TestSuite(map(isFirstLine, testcasesIsFirstLine))

##########################################################

class isLastLine(unittest.TestCase):
    """ Test cases of isLastLine """
        
    def isFirst(self):
        """ Test that when it is the first line it returns properly """
        line = FileLine(0, ["", "", ""])
        self.assertFalse(line.isLastLine())
        
    def isMiddle(self):
        """ Test that when it is the middle line it returns properly """
        line = FileLine(1, ["", "", ""])
        self.assertFalse(line.isLastLine())
        
    def isLast(self):
        """ Test that when it is the last line it returns properly """
        line = FileLine(2, ["", "", ""])
        self.assertTrue(line.isLastLine())

# Collect all test cases in this class
testcasesIsLastLine = ["isFirst", "isMiddle", "isLast"]
suiteIsLastLine = unittest.TestSuite(map(isLastLine, testcasesIsLastLine))

##########################################################

class previous(unittest.TestCase):
    """ Test cases of previous """
        
    def atFirstLine(self):
        """ Test that getting the previous line at the first line returns properly """
        line = FileLine(0, ["", "", ""])
        previousLine = line.previous()
        self.assertIs(None, previousLine)
        
    def notFirstLine(self):
        """ Test that getting the previous line returns properly """
        originalLineNumber = 1
        line = FileLine(originalLineNumber, ["", "", ""])
        previousLine = line.previous()
        self.assertEquals(originalLineNumber-1, previousLine.lineIndex)

# Collect all test cases in this class
testcasesPrevious = ["atFirstLine", "notFirstLine"]
suitePrevious = unittest.TestSuite(map(previous, testcasesPrevious))

##########################################################

class next(unittest.TestCase):
    """ Test cases of next """
        
    def atLastLine(self):
        """ Test that getting the next line at the last line returns properly """
        line = FileLine(2, ["", "", ""])
        nextLine = line.next()
        self.assertIs(None, nextLine)
        
    def notLastLine(self):
        """ Test that getting the next line returns properly """
        originalLineNumber = 1
        line = FileLine(originalLineNumber, ["", "", ""])
        nextLine = line.next()
        self.assertEquals(originalLineNumber+1, nextLine.lineIndex)

# Collect all test cases in this class
testcasesNext = ["atLastLine", "notLastLine"]
suiteNext = unittest.TestSuite(map(next, testcasesNext))

##########################################################

# Collect all test cases in this file
suites = [suiteIsFirstLine,
          suiteIsLastLine,
          suitePrevious,
          suiteNext]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)