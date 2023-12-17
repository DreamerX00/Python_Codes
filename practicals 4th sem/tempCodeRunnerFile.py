import random

def fitness_function(genes):
   
    return sum(genes)


def create_binary_gene(length):
    
    return [random.randint(0, 1) for _ in range(length)]

def crossover_binary(parent1, parent2):
    
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate_binary(gene, mutation_rate):
    
    mutated_gene = gene[:]
    for i in range(len(mutated_gene)):
        if random.random() < mutation_rate:
            mutated_gene[i] = 1 if mutated_gene[i] == 0 else 0
    return mutated_gene


def create_real_valued_gene(length, lower_bound, upper_bound):
    
    return [random.uniform(lower_bound, upper_bound) for _ in range(length)]

def crossover_real_valued(parent1, parent2):
    
    alpha = random.random()
    child1 = [alpha * p1 + (1 - alpha) * p2 for p1, p2 in zip(parent1, parent2)]
    child2 = [alpha * p2 + (1 - alpha) * p1 for p1, p2 in zip(parent1, parent2)]
    return child1, child2

def mutate_real_valued(gene, mutation_rate, lower_bound, upper_bound):
    
    mutated_gene = gene[:]
    for i in range(len(mutated_gene)):
        if random.random() < mutation_rate:
            mutated_gene[i] += random.uniform(lower_bound, upper_bound)
            mutated_gene[i] = max(lower_bound, min(upper_bound, mutated_gene[i]))
    return mutated_gene


def genetic_algorithm(gene_length, gene_type, population_size, fitness_function, crossover_function, mutation_function,
                      mutation_rate, lower_bound=None, upper_bound=None, max_generations=100):
    population = []
    for _ in range(population_size):
        if gene_type == "binary":
            gene = create_binary_gene(gene_length)
        elif gene_type == "real-valued":
            gene = create_real_valued_gene(gene_length, lower_bound, upper_bound)
        population.append(gene)

    for generation in range(max_generations):
        
        fitness_values = [fitness_function(gene) for gene in population]

        
        parent1 = population[fitness_values.index(max(fitness_values))]
        parent2 = random.choice(population)

        
        child1, child2 = crossover_function(parent1, parent2)

        
        child1 = mutation_function(child1, mutation_rate, lower_bound, upper_bound)
        child2 = mutation_function(child2, mutation_rate, lower_bound, upper_bound)

        
        min_fitness = min(fitness_values)
        min_index = fitness_values.index(min_fitness)
        population[min_index] = child1
        population[fitness_values.index(min(fitness_values))] = child2

    
    fitness_values = [fitness_function(gene) for gene in population]
    best_index = fitness_values.index(max(fitness_values))
    return population[best_index]


gene_length = 10
population_size = 100
mutation_rate = 0.1
lower_bound = -10
upper_bound = 10
best_gene = genetic_algorithm(gene_length, "real-valued", population_size, fitness_function, crossover_real_valued,
                              mutate_real_valued, mutation_rate, lower_bound, upper_bound)
print("Best gene:", best_gene)
print("Fitness value:", fitness_function(best_gene))
