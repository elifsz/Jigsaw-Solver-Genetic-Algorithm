import numpy as np
from skimage.util import view_as_blocks
from skimage.util import montage 
from skimage.transform import resize
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray
import random
import time

img = io.imread('photo.jpg')
puzzle = rgb2gray(img)
puzzle = resize(puzzle, (300,300))

puzzle_shape = (100,100)
puzzle_blocks = view_as_blocks(puzzle, block_shape = puzzle_shape)
puzzle_blocks = puzzle_blocks.reshape((-1,)+ puzzle_shape)

length = puzzle_blocks.shape[0]

Dict = {}
for i in range(0,puzzle_blocks.shape[0]):
	Dict[i] = puzzle_blocks[i]
class Genetic:
    def __init__(self, Target, Population_Number):
        self.Gene_Pool = np.arange(9)
        self.Target = Target
        self.Population_Number = Population_Number
        self.Target_Lenght = len(Target)
        self.Population = []
        self.Next_Generation = []
        self.Found = False
        self.Generation_Timer = 0

    class Member:
        def __init__(self,chromosome):
            self.Chromosome = chromosome
            self.Fitness = 0

    def random_gene(self):
        Gene = random.choice(self.Gene_Pool)
        return Gene

    def create_chromosome(self):
        Chromosome = np.arange(length)        
        np.random.shuffle(Chromosome)
        return Chromosome

    def calculate_fitness(self):
        for Member in self.Population:
            Member.Fitness = 0
            for i in range(self.Target_Lenght):
                if Member.Chromosome[i] == self.Target[i]:
                    Member.Fitness += 1

            if Member.Fitness == self.Target_Lenght:
                self.Found_Target = Member.Chromosome
                self.Found = True

    def crossover(self):
        last_best = int(( 90 * self.Population_Number) / 100)

        self.Next_Generation = []
        self.Next_Generation.extend(self.Population[last_best:])
        image_best = []


        while True:
            if len(self.Next_Generation) < self.Population_Number:
                member_1 = random.choice(self.Population[last_best:]).Chromosome
                member_2 = random.choice(self.Population[last_best:]).Chromosome
                new_member = []
                while True:
                    new_member = list(dict.fromkeys(new_member))
                    for gene1,gene2 in zip(member_1, member_2):
                        prob = random.random() # 0 - 1
                        if prob < 0.47:
                            new_member.append(gene1)
                        elif prob < 0.94:
                            new_member.append(gene2)
                        else:
                            new_member.append(self.random_gene())
                    new_member = list(dict.fromkeys(new_member))
                    if length == len(new_member):
                        break
                self.Next_Generation.append(self.Member(new_member))

            else:
                break

        self.Population = self.Next_Generation



    def main(self):
        start_time = time.time()
        for i in range(self.Population_Number):
            self.Population.append(self.Member(self.create_chromosome()))


        while not self.Found:
            self.calculate_fitness()
            self.Population = sorted(self.Population, key=lambda Member: Member.Fitness)
            image_best = []
            for block in self.Population[Population_Number-1].Chromosome:
                image_best.append(Dict[block])
            puzzle_montage = montage(image_best)
            ig = plt.figure(figsize=(10,10))
            plt.title("Best for " + str(self.Generation_Timer+1) + ". Generation")
            plt.imshow(puzzle_montage,cmap=plt.cm.gray)
            self.crossover()
            self.Generation_Timer += 1

        print("Generation: " + str(self.Generation_Timer))
        print("Execution time " + str(time.time() - start_time))

Target = list(Dict.keys())
Population_Number = 100

Go = Genetic(Target, Population_Number)
Go.main()