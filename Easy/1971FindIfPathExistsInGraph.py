class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        # for every vertex get it's neighbors
        neighbors = dict()
        for v1, v2 in edges:
            neighbors[v1] = neighbors.get(v1, []) + [v2]
            neighbors[v2] = neighbors.get(v2, []) + [v1]

        visited = set()
        q = collections.deque([source])

        # BFS to find if there is a path from source to destination
        while q:
            vertex = q.popleft()
            if vertex == destination:
                return True

            visited.add(vertex)
            for neighbor in neighbors[vertex]:
                if neighbor not in visited:
                    q.append(neighbor)

        return False
