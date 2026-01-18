class Team:
    def __init__(self,name,points=0):
        self.name = name
        self.points = points
        self.team=[]
        self.matches=0
        self.wins=0
        self.losses=0
        self.draws=0
    def get_members(self):
        return self.team
    def get_points(self):
        return self.points
    def get_name(self):
        return self.name
    def add_member(self,member):
        self.team.append(member)
    def add_point(self,point):
        self.points += point
    def set_name(self,name):
        self.name = name
    def contains_member(self,member):
        return member in self.team
    def remove_member(self,member):
        self.team.remove(member)
Ranking=[]
Wedstrijden=[]
points_draw=1
points_win=3
def add_team(team):
    Ranking.append(team)
def find_team(name):
    NL=[]
    for team in Ranking:
        NL.append(team.name)
    if name in NL:
        print(name)
    if name not in NL:
        print(None)

def add_draw(team1,team2):
    Wedstrijden.append(f'{team1.name} tegen {team2.name}: Deze wedstijd eindigde in een gelijkspel.')
    team1.draws += 1
    team2.draws += 1
    team1.points+= points_draw
    team2.points+= points_draw
    team1.matches += 1
    team2.matches += 1
def add_victory(team1):
    Wedstrijden.append(f'{team1.name}: Deze ploeg heeft die wedstrijd gewonnen.')
    team1.wins += 1
    team1.points+= points_win
    team1.matches += 1
Ranking=sorted(Ranking, key=lambda team: team.points, reverse=True)
def get_Ranking(name=Ranking):
    print('-'*17)
    for team in Ranking:
        print(f'|{Ranking.index(team)+1}|{team.name}|{team.matches}|{team.points}|{team.wins}|{team.draws}|')
        print('-'*17)
def get_Wedstrijden(name=Wedstrijden):
    for wedstrijd in Wedstrijden:
        print('-'*50)
        print(f'|{wedstrijd}|')
    print('-'*50)

#code werkt, testen moet via eigen commando's
#decoreren van klassement en ranking kan zoals bij loonfiche, de mensen mogen zelf eens kiezen of ze het aanpassen
# enkel ranking en points_draw/win is gevraagd, rest is wat gissen wat de prof bedoeldé