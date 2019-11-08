"""
https://cs.stackexchange.com/questions/87631/reservoir-sampling-algorithm-probability/87633
"""

import random
from statistics import mean


class ReservoirSampling(object):

    def __init__(self, max_size):
        self.reservoir = []
        self.max = max_size
        self.i = 0

    def add(self, element):
        size = len(self.reservoir)

        if size >= self.max:
            spot = random.randint(0, self.i - 1)
            if spot < size:
                self.reservoir[spot] = element

        else:
            self.reservoir.append(element)

        self.i += 1


class Trial(object):
    def __init__(self, data_set, sample_size, trials):
        self.data = data_set
        self.max = sample_size
        self.trials = trials
        self.cats = []
        self.dogs = []
        self.cat_average = 0
        self.dog_average = 0

        self.run()
        self.get_average()
        print(f"Cats: {self.cat_average}")
        print(f"Dogs: {self.dog_average}")

    def run(self):

        count = 0

        while count < self.trials:

            rs = ReservoirSampling(self.max)
            for pet in data:
                rs.add(pet)

            self.cats.append(rs.reservoir.count('cat'))
            self.dogs.append(rs.reservoir.count('dog'))
            count += 1

    def get_average(self):
        self.cat_average = "{:.2%}".format((mean(self.cats) / self.max))
        self.dog_average = "{:.2%}".format((mean(self.dogs) / self.max))


data_1 = ['dog'] * 100
data_2 = ['cat'] * 100
data = data_1 + data_2

rs = ReservoirSampling(1)

for pet in data:
    rs.add(pet)

print(rs.reservoir.count('cat'))
print(rs.reservoir.count('dog'))

# Trail(<data_set>, <sample size>, <number of runs>)
t = Trial(data, 200, 100)
