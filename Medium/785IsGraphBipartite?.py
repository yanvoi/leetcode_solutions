# good old BFS on the graph
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        coloring = dict()

        for node in range(len(graph)):
            if node in coloring: continue

            coloring[node] = 0
            q = collections.deque([node])
            while q:
                v = q.popleft()
                for adj in graph[v]:
                    if adj not in coloring:
                        coloring[adj] = not coloring[v]
                        q.append(adj)
                    elif coloring[adj] == coloring[v]:
                        return False

        return True
