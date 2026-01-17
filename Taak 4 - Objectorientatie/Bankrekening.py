class BankRekening:
    def __init__(self,nm,rkn,bd=0):
        self.nm=nm
        self.rkn=rkn
        self.bd=bd
    def __str__(self):
        return f'{self.nm}, {self.rkn}, bedrag: {self.bd}'
    def storten(self,bd):
        self.bd+=bd
    def afhalen(self,bd):
        self.bd-=bd
    def __repr__(self):
        return f"BankRekening('{self.nm}', '{self.rkn}', {self.bd})"