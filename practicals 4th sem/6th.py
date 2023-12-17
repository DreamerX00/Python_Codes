import random

# Define the objective function to be optimized
def objective_function(x, y):
    return (x ** 2) + (y ** 2)

# Generate a random initial solution within the search space
def generate_random_solution():
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    return x, y

# Generate all neighboring solutions from a given solution
def generate_neighbors(x, y, step_size):
    neighbors = []
    neighbors.append((x + step_size, y))  # right neighbor
    neighbors.append((x - step_size, y))  # left neighbor
    neighbors.append((x, y + step_size))  # top neighbor
    neighbors.append((x, y - step_size))  # bottom neighbor
    return neighbors

# Hill Climbing algorithm
def hill_climbing():
    current_solution = generate_random_solution()
    current_value = objective_function(current_solution[0], current_solution[1])
    
    while True:
        neighbors = generate_neighbors(current_solution[0], current_solution[1], 0.1)
        best_neighbor = current_solution
        best_value = current_value
        
        for neighbor in neighbors:
            neighbor_value = objective_function(neighbor[0], neighbor[1])
            if neighbor_value < best_value:
                best_neighbor = neighbor
                best_value = neighbor_value
        
        if best_value >= current_value:
            break
        
        current_solution = best_neighbor
        current_value = best_value
    
    return current_solution, current_value

# Steepest Ascent Hill Climbing algorithm
def steepest_ascent_hill_climbing():
    current_solution = generate_random_solution()
    current_value = objective_function(current_solution[0], current_solution[1])
    
    while True:
        neighbors = generate_neighbors(current_solution[0], current_solution[1], 0.1)
        best_neighbor = current_solution
        best_value = current_value
        
        for neighbor in neighbors:
            neighbor_value = objective_function(neighbor[0], neighbor[1])
            if neighbor_value < best_value:
                best_neighbor = neighbor
                best_value = neighbor_value
        
        if best_value >= current_value:
            break
        
        current_solution = best_neighbor
        current_value = best_value
    
    return current_solution, current_value

# Test the algorithms
print("Hill Climbing:")
solution, value = hill_climbing()
print("Solution:", solution)
print("Objective value:", value)

print("\nSteepest Ascent Hill Climbing:")
solution, value = steepest_ascent_hill_climbing()
print("Solution:", solution)
print("Objective value:", value)
