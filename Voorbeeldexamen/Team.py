class Team:
    def __init__(self, nm, pt=0):
        self.mb=[]
        self.nm = nm
        self.pt = pt
    def get_members(self):
        return self.mb
    def get_name(self):
        return self.nm
    def get_point(self):
        return self.pt
    def add_points(self, p):
        self.pt+=p
    def set_name(self, nm):
        self.nm=nm
    def add_member(self,mb):
        self.mb.append(mb)
    def contains_member(self,mb):
        return mb in self.mb
    def remove_member(self,mb):
        self.mb.remove(mb)