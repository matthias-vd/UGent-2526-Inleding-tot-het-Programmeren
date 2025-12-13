class Vertegenwoordiger:
    def __init__(self,str='',flt=0.0):
        self.str=str
        self.flt=flt
    def getNaam(self):
        return self.str
    def setNaam(self,str):
        self.str=str
    def getOmzet(self):
        return self.flt
    def setOmzet(self,flt):
        self.flt=flt
    def __str__(self):
        return f"Vertegenwoordiger[naam='{self.str}', omzet={self.flt}]"