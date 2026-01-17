class Geld:
    def __init__(self,bedrag):
        if isinstance(bedrag,Geld):
            self.euros=bedrag.euros
            self.centen=bedrag.centen
        if isinstance(bedrag,int):
            self.euros=bedrag
            self.centen=0
            if bedrag<0:
                print('Negatieve bedragen zijn niet toegelaten')
        if isinstance(bedrag,float):
            self.euros=int(bedrag*100//100)
            self.centen=int(bedrag*100%100)
            if bedrag<0:
                print('Negatieve bedragen zijn niet toegelaten')
        if isinstance(bedrag,str):
            if bedrag[0]!='€':
                print('Opmaak Geld string niet correct')
                self.euros=0
                self.centen=0
            elif bedrag[0]=='€':
                bd1=bedrag.split(',')
                for i,e in enumerate(bd1):
                    elx=''
                    for el in e:
                        if el.isdigit():
                            elx+=el
                    if i==0:
                        self.euros=int(elx)
                    if i==1:
                        self.centen=int(elx)
    def __str__(self):
        if self.centen==0 and self.euros!=0:
            return '€'+str(self.euros)+'.00'
        return '€'+str(self.euros)+'.'+str(self.centen)
    def vermenigvuldig(self,n):
        bedragv=round((self.euros*100+self.centen)*n,0)
        self.euros=int(bedragv//100)
        self.centen=int(bedragv%100)
        return self
    def optellen(self,other):
        if self.centen+other.centen<100:
            self.euros+=other.euros
            self.centen+=other.centen
            return self
        self.euros+=other.euros+1
        self.centen+=other.centen-100
        return self