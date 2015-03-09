import unittest

from caper_vault.caper_vault import CaperVault

class store(unittest.TestCase):
    """ Test cases of store """
    
    def setUp(self):
        """ Build the Vault for the test """
        self.vault = CaperVault()
        
    def firstStore(self):
        """ Test that during the first store all the variables get added """
        lineNumber = 0
        variables = {'a':1, 'b':2}
        self.vault.store(lineNumber, variables)
        self.assertEqual(variables, self.vault.states[lineNumber])
        
    def noChange(self):
        """ Test that when the variables do not change no new state is stored """
        lineNumber = 1
        variables = {'a':1, 'b':2}
        self.vault.store(0, variables)
        self.vault.store(lineNumber, variables)
        self.assertEqual({}, self.vault.states[lineNumber])
        
    def newVariable(self):
        """ Test that when a new variable is added its state is added """
        lineNumber = 1
        startVariables = {'a':1, 'b':2}
        newVariables = {'c':1}
        self.vault.store(0, startVariables)
        self.vault.store(lineNumber, newVariables)
        self.assertEqual(newVariables, self.vault.states[lineNumber])
        
    def changedVariable(self):
        """ Test that when a variable cahnges value it is added """
        lineNumber = 1
        startVariables = {'a':1, 'b':2}
        newVariables = {'a':2}
        self.vault.store(0, startVariables)
        self.vault.store(lineNumber, newVariables)
        self.assertEqual(newVariables, self.vault.states[lineNumber])

# Collect all test cases in this class
testcasesStore = ["firstStore", "noChange", "newVariable", "changedVariable"]
suiteStore = unittest.TestSuite(map(store, testcasesStore))

##########################################################

# Collect all test cases in this file
suites = [suiteStore]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)