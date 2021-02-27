# Genetic Algorithm
# created by Kirisada
# Kritsada Lueng-on
# CSIT 6024631002

import random

N = 8 # Number of Queens.
POPULATION = 4 # Population size.
GENERATION = 10 # Arbitrary number of test cycles.
MUTATION_RATE = 0.01 # Mutation Rate. 

class Chromosome:
    def __init__(self, Length):
        self.chroLength = Length

        self.chroData = [0] * Length
        for i in range(self.chroLength):
            self.chroData[i] = i
        return 
    def get_data(self):
        return self.chroData

class NQueen:
    def __init__(self, Length, nPopulation, Generation, MutationRate):
        self.qLength = Length   # Number of Queens.
        self.qnPop = nPopulation # Population size.
        self.qGen = Generation  # Arbitrary number of test cycles.
        self.qMu_Rate = MutationRate # Mutation Rate.

        self.nextMutation = 0 # For scheduling mutations.
        self.mutations = 0
        self.countGen = 0
        self.population = []
        self.possible_pairs = int(Length * (Length - 1) / 2) # Possible pairs of non attacking queens.
        return


    def initialise_population(self):
        for i in range(self.qnPop):
            newChromo = Chromosome(self.qLength).get_data()
            random.shuffle(newChromo)
            self.population.append(newChromo)
        print("Initialise Population///////////////////")
        print()
        for pop in range(self.qnPop):
                    genome = self.population[pop]
                    print("Genome[", pop, "]", ":", genome)
        print("////////////////////////////////////////")
        return

    def get_fitness(self):
        self.maxFitness = 0
        print("Fitness Function////////////////////////")
        print()
        sumFitness = 0
        for pop in range(self.qnPop):
            genome = self.population[pop]
            print("Genome[", pop, "]", ":", genome)
            sumFitness = 0
            for i in range(0, self.qLength):
                for j in range(i+1, self.qLength):
                    #          <-->                           (↖)                             (↗)
                    if(genome[i] != genome[j] and genome[i]+i != genome[j]+j and genome[i]-i != genome[j]-j):
                        sumFitness += 1
            if self.maxFitness < sumFitness:
                self.maxFitness = sumFitness
            print("sumFitness : ",sumFitness)
            print("-------------------------------------")
        print("Max Fitness :", self.maxFitness)
        print("/////////////////////////////////////////")
        return
    
    def selectionF(self):
        self.selection = []
        #print("Selection////////////////////////////////")
        #print()
        for i in range(self.qnPop):
            self.selection.append(random.choice(self.population))
        
        #for i in range(self.qnPop):
        #    print("Genome[", i, "]", ":", self.selection[i])

        #print("/////////////////////////////////////////")
        return

    def cross_over(self):
        #print("Cross-Over///////////////////////////////")
        #print()
        cross_genome = []
        
        for a in range(int(self.qnPop / 2)):
            cross = random.randint(1, self.qnPop)
            cross_genomeA = []
            cross_genomeB = []
            #print("CrossGemome:", cross_genome)
        #    print("Crossnum", cross)
        #    print("------------------------------------")
        #    print("Genome [", a+a, "]", self.selection[a+a])
        #    print("Genome [", a+a+1, "]", self.selection[a+a+1])
        #    print("////////////////////////////////") 
            # Swap them.
            for front in range(cross):
                cross_genomeA.append(self.selection[a+a][front])
                cross_genomeB.append(self.selection[a+a+1][front])
            
            for back in range(cross, self.qLength):
                cross_genomeA.append(self.selection[a+a+1][back])
                cross_genomeB.append(self.selection[a+a][back])
            cross_genome.append(cross_genomeA)
            cross_genome.append(cross_genomeB)
        #    print("Cross_Genome A:", cross_genomeA)
        #    print("Cross_Genome B:", cross_genomeB)
        self.population.clear()
        self.population = cross_genome.copy()
        print("----------------------------")
        #print("Cross_Genome :", cross_genome)
        #for n in range(self.qnPop):
        #    print("Cross_Genome [", n, "] :", cross_genome[n])
        print("----------------------------")
        print("====================================")
        
        return

    def mutationF(self):
        next

    def genetic_algorithm(self):
        popSize = 0
        done = False

        #self.mutation = 0
        #self.nextMutation = random.randrange(0, self.math_round(1.0 / self.qMu_Rate))

        while not done:
            popSize = len(self.population)
            for i in range(popSize):
                if self.countGen == self.qGen:
                    done = True
            print("GEN [", self.countGen, "] /////////////////////////////////////////////////////////")

            self.get_fitness()
            self.selectionF()
            self.cross_over()
            self.mutationF()
            self.countGen += 1
            
        print("Completed")
        print("Max Fitess :", self.maxFitness)
        print("Possible pairs :", self.possible_pairs)
        print("Generation :", self.qGen)

if __name__ == '__main__':
    nq1 = NQueen(N, POPULATION, GENERATION, MUTATION_RATE)
    nq1.initialise_population()
    nq1.genetic_algorithm()