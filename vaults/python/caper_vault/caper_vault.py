
class CaperVault:
    """ Represents a store that tracks all variable changes in a caper traacked function """
    
    def __init__(self):
        """ Initialize the vault """
        self.states = {}
        self.previousState = None
        
    def store(self, lineNumber, variables):
        """ Store the state of the variables on the given line """
        self.states[lineNumber] = {}
        for varName in variables:
            if self.shouldStore(varName, variables):
                self.states[lineNumber][varName] = variables[varName]
                
        self.previousState = variables
        
    def shouldStore(self, varName, variables):
        """ Return if the variable with the given name should be stored """
        return self.previousState is None \
            or varName not in self.previousState \
            or self.previousState[varName] != variables[varName]