import os

class CaperFunctionCaller:
    """ Responsible for creating the code to run a caper function """
    VAULT_VAR = "__caper_vault__"
    
    def __init__(self, caperFunction, startingLineNumber):
        """ Initialize with the caper function to call """
        self.caperFunction = caperFunction
        self.startingLineNumber = startingLineNumber
    
    @property
    def lines(self):
        """ Return the lines to use to call the Caper Function """
        callLine = self.caperFunction.getFnCall({self.caperFunction.VAULT_VAR: self.VAULT_VAR})
        return self.getCaller(callLine).split('/n')
        
    def getCaller(self, callLine):
        """ Get the Caller Text """
        return ("if __name__ == '__main__':" + "\n"\
                "    import sys" + "\n"\
                "    sys.path.insert(0, '{vaultsLib}')" + "\n"\
                "    from caper_vault import CaperVault" + "\n"\
                "    {vault} = CaperVault({lineNumber})" + "\n"\
                "    {callCaperFn}" + "\n"\
                "    print({vault}.states)").format(vaultsLib=self.getPythonVaultsLibDir(), vault=self.VAULT_VAR, callCaperFn=callLine, lineNumber=self.startingLineNumber)
               
    def getPythonVaultsLibDir(self):
        """ Return the directory that contains the Caper Vaults Python Package """
        path = os.path.relpath(os.path.dirname(__file__))
        return os.path.join(path, '../../../vaults/python')