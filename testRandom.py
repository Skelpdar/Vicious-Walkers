from LinConGenerator import LinConGenerator

import matplotlib.pyplot as plt

gen = LinConGenerator(12)

values = []

for _ in range(0, 1000000):
    values.append(gen.randUniform())

plt.title("Uniform distribution from Park-Miller LCG")

plt.xlabel("Value")
plt.ylabel("# of values")

plt.hist(values, bins=100)
plt.show()
plt.xlabel("x_n")
plt.ylabel("x_(n+1)")
plt.title("Density of x_n vs x_(n+1) values")
h = plt.hist2d(values[:-2],values[1:-1], bins=20, vmin=0)
plt.colorbar(h[3])
plt.show()

intvalues = []
for _ in range(0, 100000):
    intvalues.append(gen.randInteger(0,4))

plt.title("Random integers 0-3 using Park-Miller LCG")

plt.xlabel("Value")
plt.ylabel("# of values")

plt.hist(intvalues,bins=[0,1,2,3,4])
plt.xticks([0,1,2,3])
plt.show()
