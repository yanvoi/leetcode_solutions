class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        self.hasApple = hasApple
        self.adj = dict()
        for x, y in edges:
            self.adj[x] = self.adj.get(x, []) + [y]
            self.adj[y] = self.adj.get(y, []) + [x]

        self.visited = set()
        # -2 because we start from the root
        return max(self.__dfs__(0) - 2, 0)


    def __dfs__(self, vertex):

        if vertex in self.visited: return 0
        self.visited.add(vertex)

        children_sum = 0
        for child in self.adj[vertex]:
            children_sum += self.__dfs__(child)

        if children_sum > 0:
            return 2 + children_sum

        return 2 if self.hasApple[vertex] else 0
