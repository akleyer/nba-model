class Player():

    def __init__(self, name, team, gp, min, orb, to, efg):
        self.name = name
        self.team = team
        self.mins = min * gp
        self.efg = efg
        self.tov = to
        self.orb = orb

    def get_name(self):
        return self.name

    def get_efg(self):
        return self.efg

    def get_orb(self):
        return self.orb

    def get_tov(self):
        return self.tov

    def get_efg_d(self):
        return self.opp_efg

    def get_orb_d(self):
        return self.opp_orb

    def get_tov_d(self):
        return self.opp_to

    def get_min(self):
        return self.mins

    def set_opp_to(self, to):
        self.opp_to = to

    def set_opp_efg(self, efg):
        self.opp_efg = efg

    def set_opp_orb(self, orb):
        self.opp_orb = orb

    def get_opp_tov(self):
        return self.opp_to

    def get_opp_efg(self):
        return self.opp_efg

    def get_opp_orb(self):
        return self.opp_orb
