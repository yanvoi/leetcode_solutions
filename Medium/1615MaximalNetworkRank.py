class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(set)
        for a, b in roads:
            adj[a].add(b)
            adj[b].add(a)

        return max(len(adj[a]) + len(adj[b]) - (b in adj[a]) for a in range(n) for b in range(a + 1, n))
