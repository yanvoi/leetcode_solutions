class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        self.seats = seats
        self.tree = [[] for _ in range(len(roads) + 1)]
        for a, b in roads:
            self.tree[a].append(b)
            self.tree[b].append(a)

        self.answer = 0
        self.__dfs__(0, -1)
        return self.answer

    
    def __dfs__(self, node, prev):

        count = 1
        for adj in self.tree[node]:
            if adj != prev:
                count += self.__dfs__(adj, node)

        # update of the answer means how many cars will go UP the three so we skip the capital
        if node: self.answer += math.ceil(count / self.seats)
        return count
