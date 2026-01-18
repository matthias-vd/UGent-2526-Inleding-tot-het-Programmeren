class Team:
    def __init__(self,name,points=0):
        self.name = name
        self.points = points
        self.members = []


    # Accessors
    def get_members(self):
        return self.members
    def get_name(self):
        return self.name
    def get_points(self):
        return self.points


    # Mutators
    def add_points(self,amount):
        self.points += amount
    def set_name(self,newName):
        self.name=newName
    def add_member(self,name):
        self.members.append(name)

    # Extra methodes
    def contains_member(self,name):
        return name in self.members
    def remove_member(self,name):
        self.members.remove(name)