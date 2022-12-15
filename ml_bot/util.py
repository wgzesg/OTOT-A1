from random import choices
from collections import Counter
population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
million_samples = choices(population, weights, k=10**6)
def get_random_population(probablity):
    pop = choices(population, probablity, k=100)
    return Counter(pop)

