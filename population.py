import random


class Chromosome:
    size = None

    def __init__(self):
        # self.gene = [0,0,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,1,0,1,0]
        self.gene = []
        self.actual_value_x: float = 0
        self.actual_value_y: float = 0
        for i in range(0, self.size):
            number = random.choice([0, 1])
            self.gene.append(number)

    def set_actual_value_x(self, value):
        self.actual_value_x = value

    def set_actual_value_y(self, value):
        self.actual_value_y = value

    def only_add_gen(self, best_gens: list):
        self.gene = []
        self.actual_value_x: float = 0
        self.actual_value_y: float = 0
        for i in range(0, len(best_gens)):
            self.gene.append(best_gens[i])


class Individual:

    def __init__(self):
        self.chromosome: Chromosome = None

    def add_chromosome(self, new_chromosome: Chromosome):
        self.chromosome = new_chromosome

    def display(self):
        # print(f"Rozmiar chromosoma: {self.chromosome.size}")
        print(f"Lancuch genowy: {self.chromosome.gene}")
        print(f"Wartosc x: {self.chromosome.actual_value_x}")
        print(f"Wartosc y: {self.chromosome.actual_value_y}")


class Population:

    def __init__(self, amount_of_individuals: int):
        self.individual_amount: int = amount_of_individuals
        self.individuals = []
        for i in range(0, amount_of_individuals + 1):
            new_individual = Individual()
            self.individuals.append(new_individual)