class Galgje:
    def __init__(self,woord,beurten='e'):
        self.woord = woord
        self.woord_lower=woord.lower()
        if isinstance(beurten, int):
            self.beurten=beurten
        if isinstance(beurten, str):
            self.beurten=len(woord)
        self.te_raden=list(set(self.woord_lower))
        self.w=0
        self.repr='.'*len(woord)
        self.geprobeerd=[]
    def __repr__(self):
        if self.w==1:
            return f'Proficiat! Je hebt het woord geraden!\n{self.woord}'
        if self.beurten>1 and self.w==0:
            return f'Je hebt nog {self.beurten} beurten.\n{self.repr}'
        if self.beurten==1 and self.w==0:
            return f'Je hebt nog {self.beurten} beurt.\n{self.repr}'
        if self.beurten==0 and self.w==0:
            return f'Ai, je bent opgehangen.\n{self.woord}'
    def raadLetter(self,letter):
        if self.beurten==0:
            print('Sorry, het spel is reeds voorbij.')
        if self.beurten>0:
            assert isinstance(letter,str), 'argument is geen letter'
            assert len(letter)==1, 'argument is geen letter'
            assert letter not in self.geprobeerd, 'letter is al eens geprobeerd'
            self.geprobeerd.append(letter)
            if letter not in self.te_raden:
                self.beurten-=1
                if self.beurten==0:
                    print(f'Fout: letter {letter} komt niet voor in het woord.\nAi, je bent opgehangen.\n{self.woord}')
                if self.beurten==1:
                    print(f'Fout: letter {letter} komt niet voor in het woord.\nJe hebt nog 1 beurt.\n{self.repr}')
                if self.beurten>1:
                    print(f'Fout: letter {letter} komt niet voor in het woord.\nJe hebt nog {self.beurten} beurten.\n{self.repr}')
            if letter in self.te_raden:
                il=[]
                lr=list(self.repr)
                for i,e in enumerate(self.woord_lower):
                    if e==letter:
                        il.append(i)
                for e in il:
                    lr[e]=list(self.woord)[e]
                self.repr=''.join(lr)
                k=self.woord_lower.count(letter)
                self.te_raden.remove(letter)
                if self.repr==self.woord:
                    self.w=1
                    self.beurten=0
                    print(f'Correct: letter {letter} komt {k} keer voor in het woord.')
                    print('Proficiat! Je hebt het woord geraden!')
                    print(f'{self.repr}')
                if self.beurten==1:
                    print(f'Correct: letter {letter} komt {k} keer voor in het woord.\nJe hebt nog 1 beurt.\n{self.repr}')
                if self.beurten>1:
                    print(f'Correct: letter {letter} komt {k} keer voor in het woord.\nJe hebt nog {self.beurten} beurten.\n{self.repr}')