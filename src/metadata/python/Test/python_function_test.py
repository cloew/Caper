import unittest

from metadata.python.python_function import PythonFunction

class getHeader(unittest.TestCase):
    """ Test cases of getHeader """
        
    def noArgs(self):
        """ Test that a function with no arguments is returned properly """
        fnHeader = "def f():"
        fn = PythonFunction([fnHeader, ""])
        self.assertEquals(fnHeader, fn.getHeader())
        
    def args(self):
        """ Test that a function with arguments is returned properly """
        fnHeader = "def f(a, b):"
        fn = PythonFunction([fnHeader, ""])
        self.assertEquals(fnHeader, fn.getHeader())
        
    def whitespace(self):
        """ Test that a function with leading whitespace is returned properly """
        fnHeader = "\t\tdef f(a, b):"
        fn = PythonFunction([fnHeader, ""])
        self.assertEquals(fnHeader, fn.getHeader())
        
    def extraArgs(self):
        """ Test that building a header with additional args works properly """
        fnHeader = "\t\tdef f(a, b):"
        expected = "\t\tdef f(a, b, c):"
        fn = PythonFunction([fnHeader, ""])
        self.assertEquals(expected, fn.getHeader(additionalArguments=['c']))

# Collect all test cases in this class
testcasesGetHeader = ["noArgs", "args", "extraArgs", "extraArgs"]
suiteGetHeader = unittest.TestSuite(map(getHeader, testcasesGetHeader))

##########################################################

# Collect all test cases in this file
suites = [suiteGetHeader]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)