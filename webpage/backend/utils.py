from random import choices
from collections import Counter
from queue import PriorityQueue
population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_random_population(probablity):
    pop = choices(population, probablity, k=100)
    return Counter(pop)

def get_best_counter(last):
    pq = PriorityQueue()
    print(last)
    for i in range(10):
        pq.put(((last[i] + 1) / (i + 1), i))
    
    soldiders = 100
    res = [0] * 10
    while pq.empty() == False:
        _, i = pq.get()
        if soldiders >= last[i] + 1:
            res[i] = last[i] + 1
            soldiders -= res[i]
        else:
            break
    remain = soldiders / 10
    res = [x+remain for x in res]
    return res


