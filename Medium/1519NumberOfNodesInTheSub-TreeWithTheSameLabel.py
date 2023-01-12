class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        self.answer = [0] * n
        self.labels = labels
        self.adj = dict()
        for x, y in edges:
            self.adj[x] = self.adj.get(x, []) + [y]
            self.adj[y] = self.adj.get(y, []) + [x]

        self.__dfs__(0, -1)
        return self.answer


    def __dfs__(self, vertex, prev):

        cur = {self.labels[vertex]: 1}

        for adj in self.adj[vertex]:
            if adj == prev: continue

            for key, val in self.__dfs__(adj, vertex).items():
                cur[key] = cur.get(key, 0) + val

        self.answer[vertex] = cur[self.labels[vertex]]
        return cur
