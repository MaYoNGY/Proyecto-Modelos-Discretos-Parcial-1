class Proposicion:
    def __init__(self, p: bool, q: bool, r: bool, s: bool, t: bool):
        self.p = p
        self.q = q
        self.r = r
        self.s = s
        self.t = t

    def __str__(self):
        return f"p={self.p}, q={self.q}, r={self.r}, s={self.s}, t={self.t}"

