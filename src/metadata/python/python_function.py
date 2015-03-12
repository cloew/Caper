from .leading_whitespace import LeadingWhitespace

class PythonFunction:
    """ Represents a Python function """
    
    def __init__(self, functionLines):
        """ Initialize the Python Function with the lines of the function """
        if self.isRunnableFunction(functionLines):
            self.header = functionLines[0]
            self.body = functionLines[1:]
            self.parseHeader(self.header)
        # else:
            # raise InvalidFunctionException("The function is not runnable: " + str(functionLines))
            
    def isRunnableFunction(self, functionLines):
        """ Return if the lines represent a runnable function """
        return functionLines is not None and len(functionLines) > 1 and '(' in functionLines[0]
        
    def parseHeader(self, header):
        """ Parse the header """
        leftHeader, rightHeader = header.split('(')
        self.name = leftHeader.replace('def', '').strip()
        self.arguments = [argument.strip() for argument in rightHeader.split(')')[0].split(',') if argument.strip() != '']
        
    def getHeader(self, additionalArguments=[]):
        """ Return the function definition string """
        return "{0}def {1}({2}):".format(LeadingWhitespace(self.header), self.name, ", ".join(self.arguments+additionalArguments))
        
    def getFnCall(self, argValues, additionalArguments=[]):
        """ Return the function call string """
        return "{1}({2})".format(LeadingWhitespace(self.header), self.name, ", ".join([argValues[arg] for arg in self.arguments+additionalArguments]))