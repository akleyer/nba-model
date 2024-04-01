class Team():

    def __init__(self, tn, sc, efg, tov, orb, ft):
        self.name = tn
        self.score = sc
        self.efg = efg
        self.tov = tov
        self.orb = orb
        self.ft = ft
        self.factor = self._calc_factor_rating()
        self.player_stats = {}
        return

    def _calc_factor_rating(self):
        return ((0.5*self.efg) - (0.3*self.tov) + (0.15*self.orb) + (0.05*self.ft))

    def get_factor(self):
        return self.factor

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def get_efg(self):
        return self.efg

    def get_tov(self):
        return self.tov

    def get_orb(self):
        return self.orb

    def get_ft(self):
        return self.ft
