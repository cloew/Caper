from .leading_whitespace import LeadingWhitespace

class CaperFunction:
    """ Represents a Python function that can interact with a Caper Vault """
    VARIABLES_VAR = "__caper_variables__"
    VAR_NAME_VAR = "__caper_var_name__"
    VAULT_VAR = "__caper_vault__"
    
    def __init__(self, function):
        """ Initialize the Caper Function with the function it is wrapping """
        self.function = function
        
    @property
    def lines(self):
        """ Return the lines of the function with housekeeping to store the variable changes in the caper vault """
        return [self.function.getHeader(additionalArguments=[self.VAULT_VAR])] + self.getBodyLines()
        
    def getBodyLines(self):
        """ Return the lines from the body of the functon with the vault interaction added """
        lines = []
        
        for i, line in enumerate(self.function.body):
            lines += self.getHouseKeepingLinesFor(i, line)
            lines.append(line)
        
        lines += self.getHouseKeepingLinesFor(len(self.function.body), self.function.body[-1])
        return lines
        
    def getHouseKeepingLinesFor(self, index, line):
        """ Return the housekeeping lines for the given index and line """
        whitespace = LeadingWhitespace(line)
        housekeepingLines = self.getHousekeepingLines(index)
        return [whitespace+line for line in housekeepingLines]
            
    def getHousekeepingLines(self, lineNumber):
        """ Return the housekeeping for the given line number """
        return ("{variables} = {{}}" + "\n" +\
                "for {var_name} in [{var_name}  for {var_name} in dir() if {var_name} not in ['{vault}', '{var_name}', '{variables}']]:" + "\n" +\
                "    {variables}[{var_name}]=eval({var_name})" + "\n" +\
                "{vault}.store({lineNumber}, {variables})").format(lineNumber=lineNumber, variables=self.VARIABLES_VAR, var_name=self.VAR_NAME_VAR, vault=self.VAULT_VAR).split('\n')