class dicta:
    def __init__(self,dictkeyvalue):
        self.dictkeyvalue=dictkeyvalue
        
    def keys_a(self):
        if self.notdict():
            return list(self.dictkeyvalue.keys())
        
    def values_a(self):
        if self.notdict():                
            return list(self.dictkeyvalue.values())
        
    def notdict(self):
            if type(dictkeyvalue)!=dict:
                raise Exception(self.dictkeyvalue,"not a dictionary")
            return 1
                
    def userinput(self):
                        
        self.dictkeyvalue=eval(input())
        print(self.dictkeyvalue,type(self.dictkeyvalue))
        print(self.keys_a())
        print(self.values_a())
        
                        
    def insertion(self,k,v):
        self.dictkeyvalue[k]=v