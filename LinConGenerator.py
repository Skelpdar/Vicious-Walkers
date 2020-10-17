import math

class LinConGenerator:
    #Default to Park-Miller parameters
    def __init__(self, seed, a = 7**5, c = 0, m = 2**31 - 1):
        self.a = a
        self.c = c
        self.m = m
        self._xn = round(seed)
        if seed == 0 and c == 0:
            raise ValueError("Seed must be non-zero when c = 0")
        self._next()

    def _next(self):
        self._xn = (self.a*self._xn+self.c) % self.m

    def randUniform(self):
        self._next()
        return self._xn / self.m

    def randInteger(self, min, max):
        return math.floor(min + self.randUniform()*(max-min))
