from queue import PriorityQueue

graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 1), ('E', 6)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 4)],
    'F': []
}

def best_first_search(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))

    while not queue.empty():
        cost, node = queue.get()

        if node == goal:
            return True

        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                queue.put((weight, neighbor))

    return False


def a_star_search(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))

    while not queue.empty():
        cost, node = queue.get()

        if node == goal:
            return True

        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                
                heuristic = 0  
                total_cost = cost + weight + heuristic
                queue.put((total_cost, neighbor))

    return False


start_node = 'A'
goal_node = 'F'

print("Best First Search:")
result = best_first_search(graph, start_node, goal_node)
if result:
    print("Goal node found!")
else:
    print("Goal node not found.")

print("\nA* Search:")
result = a_star_search(graph, start_node, goal_node)
if result:
    print("Goal node found!")
else:
    print("Goal node not found.")
