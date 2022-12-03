class Graph:
    
    def __init__(self):
        self.nodes_neighbors = [[] for _ in range(1001)]
        
    def add_edge(self, first, second):
        self.nodes_neighbors[first].append(second)
        self.nodes_neighbors[second].append(first)
        
    def are_already_connected(self, first, second, visited):
        
        if first == second:
            return True
        
        for adjacent in self.nodes_neighbors[first]:
            if adjacent not in visited:
                visited.add(adjacent)
                if self.are_already_connected(adjacent, second, visited):
                    return True
                
        return False

    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = Graph()
            
        for first, second in edges:
            
            visited = set()
            if graph.are_already_connected(first, second, visited):
                return first, second
            
            graph.add_edge(first, second)
        
