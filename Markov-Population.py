# With a population of (A, B) and (C, D), where the comma represents a crossover point for the two candidates,
# this script will figure out what stat the Markov chain would be in when in a steady state.
# Expected answer would be (A, A)(A, A), (B, B)(B,B) and so on...

import random

population = [('A', 'B'), ('C', 'D')]

for i in range(0, 100):
    crossovers = []
    crossovers.append((population[0][0], population[1][1]))
    crossovers.append((population[0][1], population[1][0]))

    # replace random one
    population[random.randint(0, 1)] = crossovers[random.randint(0, 1)]

print(population)
