class BankRekening:
    def __init__(self,rekeninghouder,rekeningnummer,bedrag=0):
        self.rekeninghouder = rekeninghouder
        self.rekeningnummer = rekeningnummer
        self.bedrag = bedrag
    def __str__(self):
        return f"{self.rekeninghouder}, {self.rekeningnummer}, bedrag: {self.bedrag}"
    def storten(self, bedrag):
        self.bedrag += bedrag
    def afhalen(self, bedrag):
        self.bedrag -= bedrag
    def __repr__(self):
        return f"BankRekening('{self.rekeninghouder}', '{self.rekeningnummer}', {self.bedrag})"