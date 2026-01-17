class Verkeerslicht:
    def __init__(self,str='rood'):
        self.kl=['groen','oranje','rood']
        self.str=str
        self.ind=self.kl.index(self.str)
    def __repr__(self):
        return f"Verkeerslicht('{self.str}')"
    def __str__(self):
        return self.str
    def volgende(self):
        r=self.ind+1
        self.ind=r%3
        self.str=self.kl[self.ind]