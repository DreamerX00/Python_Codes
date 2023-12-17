import itertools
import sys

# Calculate the total distance of a given tour
def calculate_distance(tour, distance_matrix):
    total_distance = 0
    num_cities = len(tour)
    for i in range(num_cities - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_distance += distance_matrix[city1][city2]
    # Add distance from the last city back to the starting city
    total_distance += distance_matrix[tour[-1]][tour[0]]
    return total_distance

# Brute force approach to solve the TSP
def tsp_brute_force(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    best_tour = None
    best_distance = sys.maxsize
    
    # Generate all possible permutations of the cities
    all_permutations = itertools.permutations(cities)
    
    for permutation in all_permutations:
        tour = list(permutation)
        distance = calculate_distance(tour, distance_matrix)
        if distance < best_distance:
            best_distance = distance
            best_tour = tour
    
    return best_tour, best_distance

# Test the TSP brute force approach
distance_matrix = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

best_tour, best_distance = tsp_brute_force(distance_matrix)

print("Best tour:", best_tour)
print("Best distance:", best_distance)
