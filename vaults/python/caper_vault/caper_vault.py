import json

class CaperVault:
    """ Represents a store that tracks all variable changes in a caper traacked function """
    
    def __init__(self, lineNumber):
        """ Initialize the vault """
        self.startsOn = lineNumber
        self.states = []
        self.previousState = None
        self.nextLineNumber = lineNumber+1
        
    def store(self, lineNumber, variables):
        """ Store the state of the variables on the given line """
        fileLineNumber = self.getFileLineNumber(lineNumber)
        state = {'lineNumber': fileLineNumber, 'variables': {}}
        for varName in variables:
            if self.shouldStore(varName, variables):
                state['variables'][varName] = variables[varName]
        self.states.append(state)
        self.previousState = variables
        self.nextLineNumber = fileLineNumber+1
        
    def shouldStore(self, varName, variables):
        """ Return if the variable with the given name should be stored """
        return self.previousState is None \
            or varName not in self.previousState \
            or self.previousState[varName] != variables[varName]
            
    def getFileLineNumber(self, lineNumber):
        """ Returns the line number in the file given the line number in the function """
        return self.startsOn+lineNumber
            
    def setReturnValue(self, returnValue):
        """ Returns the line number in the file given the line number in the function """
        self.returnState = {'value':returnValue, 'lineNumber': self.nextLineNumber}
        
    def toJson(self):
        """ Return the state as Json """
        return json.dumps({'states':self.states, 'returned':self.returnState})