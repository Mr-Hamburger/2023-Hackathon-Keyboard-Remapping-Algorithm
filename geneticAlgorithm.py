import random
import distances

# Define the target input string
target_input = "your target input string goes here"

# Define the available keys on the keyboard
keys = list("qwertyuiopasdfghjkl;zxcvbnm,./")

# Define the population size and the number of generations
population_size = 100
num_generations = 100

# Function to generate a random keyboard layout
def generate_random_keyboard():
    random.shuffle(keys)
    return ''.join(keys)

# Function to evaluate the fitness of a keyboard layout
def evaluate_fitness(keyboard_layout):
    line1 = keyboard_layout[0:10]
    line2 = keyboard_layout[10:20]
    line3 = keyboard_layout[20:30]
    
    keyboard_layout = [line1, line2, line3]
    print(keyboard_layout)
    print("hi")
    return distances.findDist(target_input, keyboard_layout)

# Function to perform single-point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(keys) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Function to perform mutation
def mutate(individual):
    index1, index2 = random.sample(range(len(keys)), 2)
    mutated_individual = list(individual)
    mutated_individual[index1], mutated_individual[index2] = mutated_individual[index2], mutated_individual[index1]
    return ''.join(mutated_individual)

# Generate the initial population
population = [generate_random_keyboard() for _ in range(population_size)]

# Evolve the population
for generation in range(num_generations):
    # Evaluate the fitness of each individual in the population
    fitness_scores = [evaluate_fitness(individual) for individual in population]

    # Select parents for crossover using tournament selection
    parents = []
    for _ in range(population_size):
        tournament = random.sample(range(population_size), 3)
        tournament_fitness = [fitness_scores[index] for index in tournament]
        winner_index = tournament[tournament_fitness.index(min(tournament_fitness))]
        parents.append(population[winner_index])

    # Create the next generation through crossover and mutation
    next_generation = []
    for i in range(0, population_size, 2):
        parent1 = parents[i]
        parent2 = parents[i+1]
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        mutated_child1 = mutate(child1)
        mutated_child2 = mutate(child2)
        next_generation.extend([mutated_child1, mutated_child2])

    # Update the population
    population = next_generation

# Find the best keyboard layout in the final population
best_layout = min(population, key=evaluate_fitness)

# Output the best keyboard layout
print("Best keyboard layout:")
print(best_layout)

# Example usage of distance.findDist() with the best layout
distance_score = evaluate_fitness(best_layout)
print("Distance score:", distance_score)
