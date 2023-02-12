class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        self.adj = defaultdict(set)
        self.answer = [0] * n
        self.subtree_count = [1] * n
        self.n = n

        for a, b in edges:
            self.adj[a].add(b)
            self.adj[b].add(a)

        self.preorder(0, -1)
        self.postorder(0, -1)

        return self.answer

    
    def preorder(self, node, prev):
        for neighbor in self.adj[node]:
            if neighbor != prev:
                self.preorder(neighbor, node)

                self.subtree_count[node] += self.subtree_count[neighbor]
                self.answer[node] += self.answer[neighbor] + self.subtree_count[neighbor]


    def postorder(self, node, prev):
        for neighbor in self.adj[node]:
            if neighbor != prev:
                self.answer[neighbor] = self.answer[node] + self.n -  2 * self.subtree_count[neighbor]
                
                self.postorder(neighbor, node)
