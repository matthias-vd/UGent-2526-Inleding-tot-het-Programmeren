import datetime
class Rijksregisternummer:
    def __init__(self,rrn):
        assert isinstance(rrn,str), 'ongeldig type'
        rrns=''
        for e in rrn:
            if e.isdigit():
                rrns+=e
        n=len(rrns)
        if n!=11:
            assert n==1, f'ongeldig formaat ({n} cijfers)'
            assert n>1, f'ongeldig formaat ({n} cijfer)'
        self.rrns=rrns
    def __repr__(self):
        return f"Rijksregisternummer('{self.rrns}')"
    def __str__(self):
        return f"{self.rrns[:2]}.{self.rrns[2:4]}.{self.rrns[4:6]}-{self.rrns[6:9]}.{self.rrns[9:11]}"
    def geslacht(self):
        rrn69=int(self.rrns[6:9])
        if rrn69%2==1:
            return 'man'
        return 'vrouw'
    def controlegetal(self,y2k=None):
        if not y2k:
            return 97-int(self.rrns[:-2])%97
        return 97-int('2'+self.rrns[:-2])%97
    def geboortedatum(self):
        try:
            cent='19' # moet als standaard wegens oplossingen
            if self.controlegetal()==int(self.rrns[-2:]):
                cent='19'
            elif self.controlegetal(True)==int(self.rrns[-2:]):
                cent='20'
            date=datetime.date(int(cent+self.rrns[:2]),int(self.rrns[2:4]),int(self.rrns[4:6]))
            return date
        except:
            assert False, 'ongeldige geboortedatum'
    def geldig(self):
        if self.controlegetal()==int(self.rrns[-2:]) or self.controlegetal(True)==int(self.rrns[-2:]):
            try:
                self.geboortedatum()
                return True
            except:
                pass
        return False