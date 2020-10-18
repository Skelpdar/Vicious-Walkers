import numpy as np
from functools import reduce
import matplotlib.pyplot as plt

from LinConGenerator import LinConGenerator
gen = LinConGenerator(12)

class Walker:
    def __init__(self, pos, mass = 1):
        self.pos = pos
        self.mass = mass

class Board:
    def __init__(self, size):
        self.size = size
        self.dim = len(size)
        self.walkers = []

    def getPos(self, pos):
        
        newpos = []

        for k in range(0,self.dim):
            newpos.append(pos[k] % self.size[k])

        return newpos

    def isOccupied(self, pos):
        for k in self.walkers:
            if pos == k.pos:
                return True
        return False

    def newWalker(self):
        while True:
            pos = [gen.randInteger(0,self.size[k]) for k in range(0,len(self.size))]
            if not self.isOccupied(pos):
                self.walkers.append(Walker(pos))
                break

    def density(self):
        volume = reduce(lambda x, y: x * y, self.size, 1)
        return len(self.walkers)/volume

    def step(self, moves):
        #Choose walker randomly (i.e. they do not all get the opportunity to move once before any other walker does it twice)
        if len(self.walkers) > 0:
            #n = np.random.randint(0,len(self.walkers))
            n = gen.randInteger(0,len(self.walkers))

            pos = self.walkers[n].pos

            #Choose a move
            move = moves[np.random.randint(0,len(moves))]

            newpos = [pos[k] + move[k] for k in range(0,len(pos))]

            collision = self.isOccupied(newpos)

            if collision:
                #Remove moving walker
                self.walkers.pop(n)
                #Find collision target
                for i in range(0,len(self.walkers)):
                    if self.walkers[i].pos == newpos:
                        self.walkers.pop(i)
                        break
            else:
                self.walkers[n].pos = newpos

iterations = 5

avgdensity = []

for i in range(0,iterations):
    #Init board
    board = Board([100,100,100])

    #Init N walkers
    #N = int(np.ceil(0.1*reduce(lambda x, y: x * y, board.size, 1)))

    N = 1000

    for _ in range(0,N):
        board.newWalker()

    density = [] 

    steps = list(range(0,100000))
    for _ in steps:
        board.step([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
        density.append(board.density())

    volume = reduce(lambda x, y: x * y, board.size, 1)

    realTime = [0]

    for k in range(1,len(steps)):
        realTime.append(realTime[-1] + 1/(volume*density[k]))

    plt.plot(realTime,density, color='grey')

    if i == 0:
        avgdensity = density
    else:
        for k in range(0,len(density)):
            avgdensity[k] += density[k]

#plt.plot(realTime[2500:], [t**(-1) for t in realTime[2500:]], label="Thermodynamical limit")

plt.xlabel("t (abstract unit)")

plt.ylabel("Density (# particles / volume)")  
plt.plot(realTime, [k/iterations for k in avgdensity], label="Average of walks", linewidth=2)

plt.legend()

plt.show()
