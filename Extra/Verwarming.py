class Verwarming:
    def __init__(self,loc,temperatuur=10.0,minimum=0.0,maximum=100.0):
        self.loc=loc
        self.temp=temperatuur
        self.min=minimum
        self.max=maximum
    def __repr__(self):
        return f"Verwarming('{self.loc}', {self.temp:.1f}, {self.min:.1f}, {self.max:.1f})"
    def __str__(self):
        return f"{self.loc}: huidige temperatuur: {self.temp:.1f}; toegelaten min: {self.min:.1f}; toegelaten max: {self.max:.1f}"
    def wijzig_temperatuur(self,dt):
        if dt<0:
            if self.temp+dt<self.min:
                self.temp=self.min
            elif self.temp+dt>=self.min:
                self.temp+=dt
        if dt>0:
            if self.temp+dt>self.max:
                self.temp=self.max
            elif self.temp+dt<=self.max:
                self.temp+=dt
    def temperatuur(self):
        return float(f'{self.temp:.1f}')