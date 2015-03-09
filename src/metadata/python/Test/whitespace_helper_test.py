import unittest

from metadata.python.whitespace_helper import FindStartingWhitespace as findStartingWhitespace

class FindStartingWhitespace(unittest.TestCase):
    """ Test cases of FindStartingWhitespace """
    EMPTY = ""
    SPACES = "    "
    TABS = "\t"
        
    def empty(self):
        """ Test that when there is no text the whitespace is found properly """
        self.assertEqual("", findStartingWhitespace(self.EMPTY))
        
    def noText(self):
        """ Test that a line of only whitespace is found properly """
        line = "{0}".format(self.SPACES)
        self.assertEqual(self.SPACES, findStartingWhitespace(line))
        
    def spaces(self):
        """ Test that whitespace of spaces is found properly """
        line = "{0}Some Text".format(self.SPACES)
        self.assertEqual(self.SPACES, findStartingWhitespace(line))
        
    def tabs(self):
        """ Test that whitespace of tabs is found properly """
        line = "{0}Some Text".format(self.TABS)
        self.assertEqual(self.TABS, findStartingWhitespace(line))
        
    def mixed(self):
        """ Test that whitespace of tabs is found properly """
        whitespace = "{0}{1}{0}".format(self.SPACES, self.TABS)
        line = "{0}Some Text".format(whitespace)
        self.assertEqual(whitespace, findStartingWhitespace(line))

# Collect all test cases in this class
testcasesFindStartingWhitespace = ["empty", "noText", "spaces", "tabs", "mixed"]
suiteFindStartingWhitespace = unittest.TestSuite(map(FindStartingWhitespace, testcasesFindStartingWhitespace))

##########################################################

# Collect all test cases in this file
suites = [suiteFindStartingWhitespace]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)