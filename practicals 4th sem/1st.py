from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        traversal = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                neighbors = self.graph.get(vertex, [])
                queue.extend(neighbors)

        return traversal

    def dfs(self, start):
        visited = set()
        traversal = []
        self._dfs_helper(start, visited, traversal)

        return traversal

    def _dfs_helper(self, vertex, visited, traversal):
        visited.add(vertex)
        traversal.append(vertex)

        neighbors = self.graph.get(vertex, [])
        for neighbor in neighbors:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited, traversal)


graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')
graph.add_edge('E', 'G')

print("BFS traversal:", graph.bfs('A'))  
print("DFS traversal:", graph.dfs('A'))  
